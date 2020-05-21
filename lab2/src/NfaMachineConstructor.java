import java.util.Set;

public class NfaMachineConstructor {
    /**
     * nfa 的开头和结尾
     */
    public static class NfaPair {
        public Nfa startNode;
        public Nfa endNode;
    }

    private Lexer lexer;

    //get NfaNode
    private NfaManager nfaManager = null;

    public NfaMachineConstructor(Lexer lexer) throws Exception {
        this.lexer = lexer;
        nfaManager = new NfaManager();

        while (lexer.matchToken(Lexer.Token.EOS)) {
            lexer.advance();
        }
    }

    public void expr(NfaPair pairOut) throws Exception {
        /*
         * expr 由一个或多个complie 之间进行 OR 形成
         * 如果表达式只有一个complie 那么expr 就等价于complie
         * 如果表达式由多个complie做或连接构成那么 expr-> complie | complie | ....
         * 由此得到expr的语法描述为:
         * expr -> expr OR complie
         *         | complie
         *
         */
        complie(pairOut);
        NfaPair localPair = new NfaPair();

        while (lexer.matchToken(Lexer.Token.OR)) {
            lexer.advance();
            complie(localPair);

            Nfa startNode = nfaManager.newNfa();
            startNode.next2 = localPair.startNode;
            startNode.next = pairOut.startNode;
            pairOut.startNode = startNode;

            Nfa endNode = nfaManager.newNfa();
            pairOut.endNode.next = endNode;
            localPair.endNode.next = endNode;
            pairOut.endNode = endNode;
        }

    }


    public void complie(NfaPair pairOut) throws Exception {
        /*
         * complie -> factor factor .....
         * 由于多个factor 前后结合就是一个complie所以
         * complie-> factor complie
         */
        // if it can be cat

        boolean b = constructNfaABSingleCharacter(pairOut);

        if (first_in_cat(lexer.getCurrentToken())) {
            factor(pairOut);
        }

        char c = (char) lexer.getLexeme();

        while (first_in_cat(lexer.getCurrentToken())) {
            NfaPair pairLocal = new NfaPair();
            factor(pairLocal);

            pairOut.endNode.next = pairLocal.startNode;

            pairOut.endNode = pairLocal.endNode;
        }
        constructNfaAESingleCharacter(pairOut);

    }

    private boolean first_in_cat(Lexer.Token tok) throws Exception {
        switch (tok) {
            //正确的表达式不会以 ) $ 开头,如果遇到EOS表示正则表达式解析完毕，那么就不应该执行该函数
            case CLOSE_PAREN:
            case AT_EOL:
            case OR:
            case EOS:
                return false;
            case CLOSURE:
            case PLUS_CLOSE:
            case OPTIONAL:
                //*, +, ? 这几个符号应该放在表达式的末尾
                ErrorHandler.parseErr(ErrorHandler.Error.E_CLOSE);
                return false;
            case CCL_END:
                //表达式不应该以]开头
                ErrorHandler.parseErr(ErrorHandler.Error.E_BRACKET);
                return false;
            case AT_BOL:
                //^必须在表达式的最开始/
                ErrorHandler.parseErr(ErrorHandler.Error.E_BOL);

                return false;
        }
        return true;
    }

    /**
     * 以闭包为最小单位
     *
     * @param pairOut
     * @throws Exception
     */
    public void factor(NfaPair pairOut) throws Exception {
        term(pairOut);

        boolean handled = false;
        // * see it  if have the *
        handled = constructStarClosure(pairOut);

        if (handled == false) {
            // See if it contains +
            handled = constructPlusClosure(pairOut);
        }

        if (handled == false) {
            // See if it contains ? ()
            handled = constructOptionsClosure(pairOut);
        }

    }


    /**
     * construct * NFA
     * like a*
     *
     * @param pairOut
     * @return boolean
     * @throws Exception
     */
    public boolean constructStarClosure(NfaPair pairOut) throws Exception {
        Nfa start, end;

        if (lexer.matchToken(Lexer.Token.CLOSURE) == false) {
            return false;
        }

        start = nfaManager.newNfa();
        end = nfaManager.newNfa();

        start.next = pairOut.startNode;
        pairOut.endNode.next = pairOut.startNode;

        start.next2 = end;
        pairOut.endNode.next2 = end;

        pairOut.startNode = start;
        pairOut.endNode = end;

        lexer.advance();

        return true;
    }

    /**
     * construct + NFA
     * like a+
     *
     * @param pairOut
     * @return
     * @throws Exception
     */
    public boolean constructPlusClosure(NfaPair pairOut) throws Exception {
        Nfa start, end;

        if (lexer.matchToken(Lexer.Token.PLUS_CLOSE) == false) {
            return false;
        }

        start = nfaManager.newNfa();
        end = nfaManager.newNfa();

        start.next = pairOut.startNode;
        pairOut.endNode.next2 = end;
        pairOut.endNode.next = pairOut.startNode;


        pairOut.startNode = start;
        pairOut.endNode = end;

        lexer.advance();
        return true;
    }

    /**
     * Closure item? NFA
     *
     * @param pairOut
     * @return
     * @throws Exception
     */
    public boolean constructOptionsClosure(NfaPair pairOut) throws Exception {
        Nfa start, end;

        if (lexer.matchToken(Lexer.Token.OPTIONAL) == false) {
            return false;
        }

        start = nfaManager.newNfa();
        end = nfaManager.newNfa();

        start.next = pairOut.startNode;
        pairOut.endNode.next = end;

        start.next2 = end;

        pairOut.startNode = start;
        pairOut.endNode = end;

        lexer.advance();

        return true;
    }

    /**
     * 以非闭包为最小单位. 匹配完成后,然后看作一个闭包
     * term ->  character | [...] | [^...] | [character-charcter] | . | (expr)
     *
     * @param pairOut
     * @throws Exception
     */
    public void term(NfaPair pairOut) throws Exception {
        boolean handled = constructExprInParen(pairOut);
        if (handled == false) {
            handled = constructNfaForSingleCharacter(pairOut);
        }

        if (handled == false) {
            handled = constructNfaForDot(pairOut);
        }

        if (handled == false) {
            constructNfaForCharacterSet(pairOut);
        }
    }

    /**
     * construct ()
     *
     * @param pairOut
     * @return
     * @throws Exception
     */
    private boolean constructExprInParen(NfaPair pairOut) throws Exception {
        if (lexer.matchToken(Lexer.Token.OPEN_PAREN)) {
            lexer.advance();
            expr(pairOut);
            if (lexer.matchToken(Lexer.Token.CLOSE_PAREN)) {
                lexer.advance();
            } else {
                ErrorHandler.parseErr(ErrorHandler.Error.E_PAREN);
            }
            return true;
        }
        return false;
    }

    /**
     * constraint single Character NFA
     *
     * @param pairOut
     * @return
     * @throws Exception
     */
    public boolean constructNfaForSingleCharacter(NfaPair pairOut) throws Exception {
        if (lexer.matchToken(Lexer.Token.L) == false) {
            return false;
        }

        Nfa start = null;
        start = pairOut.startNode = nfaManager.newNfa();
        pairOut.endNode = pairOut.startNode.next = nfaManager.newNfa();

        start.setEdge(lexer.getLexeme());

        lexer.advance();

        return true;
    }

    /**
     * construct . NFA
     *
     * @param pairOut
     * @return
     * @throws Exception
     */
    public boolean constructNfaForDot(NfaPair pairOut) throws Exception {
        if (lexer.matchToken(Lexer.Token.ANY) == false) {
            return false;
        }

        Nfa start = null;
        start = pairOut.startNode = nfaManager.newNfa();
        pairOut.endNode = pairOut.startNode.next = nfaManager.newNfa();

        start.setEdge(Nfa.CCL);
        start.addToSet((byte) '\n');
        start.addToSet((byte) '\r');
        start.setComplement();

        lexer.advance();

        return true;
    }

    /**
     * construct [] NFA
     *
     * @param pairOut
     * @return
     * @throws Exception
     */
    public boolean constructNfaForCharacterSetWithoutNegative(NfaPair pairOut) throws Exception {

        if (lexer.matchToken(Lexer.Token.CCL_START) == false) {
            return false;
        }

        lexer.advance();

        Nfa start = null;
        start = pairOut.startNode = nfaManager.newNfa();
        pairOut.endNode = pairOut.startNode.next = nfaManager.newNfa();
        start.setEdge(Nfa.CCL);

        if (lexer.matchToken(Lexer.Token.CCL_END) == false) {
            dodash(start.inputSet);
        }

        if (lexer.matchToken(Lexer.Token.CCL_END) == false) {
            ErrorHandler.parseErr(ErrorHandler.Error.E_BADEXPR);
        }
        lexer.advance();

        return true;
    }

    /**
     * construct [^a]
     *
     * @param pairOut
     * @return
     * @throws Exception
     */
    public boolean constructNfaForCharacterSet(NfaPair pairOut) throws Exception {
        if (lexer.matchToken(Lexer.Token.CCL_START) == false) {
            return false;
        }

        lexer.advance();
        boolean negative = false;
        if (lexer.matchToken(Lexer.Token.AT_BOL)) {
            negative = true;
        }

        Nfa start = null;
        start = pairOut.startNode = nfaManager.newNfa();
        pairOut.endNode = pairOut.startNode.next = nfaManager.newNfa();
        start.setEdge(Nfa.CCL);

        if (lexer.matchToken(Lexer.Token.CCL_END) == false) {
            dodash(start.inputSet);
        }

        if (lexer.matchToken(Lexer.Token.CCL_END) == false) {
            ErrorHandler.parseErr(ErrorHandler.Error.E_BADEXPR);
        }

        if (negative) {
            start.setComplement();
        }

        lexer.advance();

        return true;
    }

    /**
     * ^
     *
     * @param pairOut
     * @return
     * @throws Exception
     */
    boolean constructNfaABSingleCharacter(NfaPair pairOut) throws Exception {

        if (lexer.matchToken(Lexer.Token.AT_BOL) || lexer.getCharIndex() == 0) {
            lexer.advance();
            constructNfaForSingleCharacter(pairOut);
        }
        return true;
    }

    /**
     * $
     *
     * @param pairOut
     * @return
     * @throws Exception
     */
    boolean constructNfaAESingleCharacter(NfaPair pairOut) throws Exception {

        if (lexer.matchToken(Lexer.Token.AT_EOL)) {
            return true;
        }
        return true;
    }

    /**
     * construct item{n, m} NFA
     *
     * @return
     */
    boolean constructNfaDefineNumCharacterSet(NfaPair pairOut) throws Exception {

        Nfa start, end;

        if (!lexer.matchToken(Lexer.Token.OPEN_CURLY)) {
            return false;
        }
        lexer.advance();
        int min = -1;
        int max = -1;
        while (!lexer.matchToken(Lexer.Token.CLOSE_CURLY) && !lexer.matchToken(Lexer.Token.EOS)) {

            if (!lexer.matchToken(Lexer.Token.COMMA)) {
                min = lexer.getLexeme() - '0';
                lexer.advance();
            } else {
                lexer.advance();
                if (!lexer.matchToken(Lexer.Token.CLOSE_CURLY)) {
                    max = lexer.getLexeme() - '0'; // infinite
                    lexer.advance();
                } else {
                    max = -1;
                }
            }
        }

        if (!lexer.matchToken(Lexer.Token.CLOSE_CURLY)) {
            throw new Exception("expressiong is error!");
        }

        lexer.advance();

        return true;
    }

    /**
     * [1 - 9] deal the dash -
     *
     * @param set
     */
    private void dodash(Set<Byte> set) {
        int first = 0;

        while (lexer.matchToken(Lexer.Token.EOS) == false &&
                lexer.matchToken(Lexer.Token.CCL_END) == false) {

            if (lexer.matchToken(Lexer.Token.DASH) == false) {
                first = lexer.getLexeme();
                set.add((byte) first);
            } else {
                lexer.advance(); //越过 -
                for (; first <= lexer.getLexeme(); first++) {
                    set.add((byte) first);
                }
            }
            lexer.advance();
        }
    }
}
