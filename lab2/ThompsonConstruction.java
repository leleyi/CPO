
public class ThompsonConstruction {

    String regularExpr = "[.]";
    private Lexer lexer = null;

    private NfaMachineConstructor nfaMachineConstructor = null;
    private NfaPrinter nfaPrinter = new NfaPrinter();


    private void runLexerExample() {
        lexer = new Lexer(regularExpr);
        int exprCount = 0;
        System.out.println("当前正则解析的正则表达式: " + regularExpr);
        lexer.advance();
        printLexResult();
    }

    private void printLexResult() {
        while (lexer.matchToken(Lexer.Token.EOS) == false) {
            System.out.println("当前识别字符是: " + (char) lexer.getLexeme());

            if (lexer.matchToken(Lexer.Token.L) != true) {
                System.out.println("当前字符具有特殊含义");

                printMetaCharMeaning(lexer);
            } else {
                System.out.println("当前字符是普通字符常量");
            }
            lexer.advance();
        }
    }

    private void printMetaCharMeaning(Lexer lexer) {
        String s = "";
        if (lexer.matchToken(Lexer.Token.ANY)) {
            s = "当前字符是点通配符";
        }

        if (lexer.matchToken(Lexer.Token.AT_BOL)) {
            s = "当前字符是开头匹配符";
        }

        if (lexer.matchToken(Lexer.Token.AT_EOL)) {
            s = "当前字符是末尾匹配符";
        }

        if (lexer.matchToken(Lexer.Token.CCL_END)) {
            s = "当前字符是字符集类结尾括号";
        }

        if (lexer.matchToken(Lexer.Token.CCL_START)) {
            s = "当前字符是字符集类的开始括号";
        }

        if (lexer.matchToken(Lexer.Token.CLOSE_CURLY)) {
            s = "当前字符是结尾大括号";
        }

        if (lexer.matchToken(Lexer.Token.CLOSE_PAREN)) {
            s = "当前字符是结尾圆括号";
        }

        if (lexer.matchToken(Lexer.Token.DASH)) {
            s = "当前字符是横杆";
        }

        if (lexer.matchToken(Lexer.Token.OPEN_CURLY)) {
            s = "当前字符是起始大括号";
        }

        if (lexer.matchToken(Lexer.Token.OPEN_PAREN)) {
            s = "当前字符是起始圆括号";
        }

        if (lexer.matchToken(Lexer.Token.OPTIONAL)) {
            s = "当前字符是单字符匹配符?";
        }

        if (lexer.matchToken(Lexer.Token.OR)) {
            s = "当前字符是或操作符";
        }

        if (lexer.matchToken(Lexer.Token.PLUS_CLOSE)) {
            s = "当前字符是正闭包操作符";
        }

        if (lexer.matchToken(Lexer.Token.CLOSURE)) {
            s = "当前字符是闭包操作符";
        }

        System.out.println(s);
    }

    private void runNfaMachineConstructorExample() throws Exception {
        lexer = new Lexer("[2-9]*qq.com");

        nfaMachineConstructor = new NfaMachineConstructor(lexer);

        NfaMachineConstructor.NfaPair pair = new NfaMachineConstructor.NfaPair();
//        nfaMachineConstructor.constructNfaForSingleCharacter(pair);
//        nfaMachineConstructor.constructNfaForCharacterSet(pair);
        nfaMachineConstructor.cat_expr(pair);
//        nfaMachineConstructor.constructNfaDefineNumCharacterSet(pair);
        nfaPrinter.printNfa(pair.startNode);

        NfaIntepretor nfaIntepretor = new NfaIntepretor(pair.startNode, "65qq.com");
        nfaIntepretor.match();

    }


    public static void main(String[] args) throws Exception {
        ThompsonConstruction construction = new ThompsonConstruction();
//        construction.runLexerExample();
        construction.runNfaMachineConstructorExample();

    }
}
