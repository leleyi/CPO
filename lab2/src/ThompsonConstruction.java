import org.junit.Test;

import java.awt.*;

public class ThompsonConstruction {

    private Lexer lexer = null;

    private NfaMachineConstructor nfaMachineConstructor = null;
    private NfaPrinter nfaPrinter = new NfaPrinter();


    /**
     * variant 6  \, ^, ., $, *, +, [ ], [^ ], { }.
     * [] [^] . * + , ^         \ ^ {} $
     *
     * @throws Exception
     */


    NfaMachineConstructor.NfaPair pair = new NfaMachineConstructor.NfaPair();


    /**
     * \\*
     *
     * @throws Exception
     */
    @Test
    public void test_star_closure() throws Exception {
        lexer = new Lexer("3*");
        nfaMachineConstructor = new NfaMachineConstructor(lexer);
        nfaMachineConstructor.complie(pair);
        NfaIntepretor nfaIntepretor = new NfaIntepretor(pair.startNode, "333");
        String o = nfaIntepretor.match();
        assert o.equals("333");
    }

    /**
     * +
     *
     * @throws Exception
     */
    @Test
    public void test_plus_closure() throws Exception {
        lexer = new Lexer("3+");
        nfaMachineConstructor = new NfaMachineConstructor(lexer);
        nfaMachineConstructor.complie(pair);
        NfaIntepretor nfaIntepretor = new NfaIntepretor(pair.startNode, "33");
        String o = nfaIntepretor.match();
        assert o.equals("33");
    }

    /***
     * \\.
     * @throws Exception
     */
    @Test
    public void test_dot_closure() throws Exception {
        lexer = new Lexer("3.");
        nfaMachineConstructor = new NfaMachineConstructor(lexer);
        nfaMachineConstructor.complie(pair);
        NfaIntepretor nfaIntepretor = new NfaIntepretor(pair.startNode, "32");
        String o = nfaIntepretor.match();
        assert o.equals("32");
    }


    /**
     * []
     *
     * @throws Exception
     */
    @Test
    public void test_CCL_closure() throws Exception {
        lexer = new Lexer("[1-9]");
        nfaMachineConstructor = new NfaMachineConstructor(lexer);
        nfaMachineConstructor.complie(pair);
        NfaIntepretor nfaIntepretor = new NfaIntepretor(pair.startNode, "8");
        String o = nfaIntepretor.match();
        assert o.equals("8");
    }

    /**
     * [^]
     *
     * @throws Exception
     */
    @Test
    public void test_ACCL_closure() throws Exception {
        lexer = new Lexer("[^1-8]");
        nfaMachineConstructor = new NfaMachineConstructor(lexer);
        nfaMachineConstructor.complie(pair);
        NfaIntepretor nfaIntepretor1 = new NfaIntepretor(pair.startNode, "9");
        NfaIntepretor nfaIntepretor2 = new NfaIntepretor(pair.startNode, "8");
        String o1 = nfaIntepretor1.match();
        String o2 = nfaIntepretor2.match();
        assert o1.equals("9");
        assert o2.equals("");

    }

    /**
     * ^
     *
     * @throws Exception
     */
    @Test
    public void test_AT_B() throws Exception {
        lexer = new Lexer("^8");
        nfaMachineConstructor = new NfaMachineConstructor(lexer);
        nfaMachineConstructor.complie(pair);
        NfaIntepretor nfaIntepretor1 = new NfaIntepretor(pair.startNode, "8.com");
        String o = nfaIntepretor1.match();
        assert "8".equals(o);
    }

    /**
     * $
     * @throws Exception
     */
    @Test
    public void test_AT_E() throws Exception {
        lexer = new Lexer("[1-9]*a$");
        nfaMachineConstructor = new NfaMachineConstructor(lexer);
        nfaMachineConstructor.complie(pair);
        NfaIntepretor nfaIntepretor1 = new NfaIntepretor(pair.startNode, "556a$");
        String o = nfaIntepretor1.match();
        System.out.println(o);
        assert "556a".equals(o);
    }

    /**
     * test match method
     *
     * @throws Exception
     */
    @Test
    public void test_match_method() throws Exception {
        lexer = new Lexer("[1-9]*qq.[a-z]*");
        nfaMachineConstructor = new NfaMachineConstructor(lexer);
        nfaMachineConstructor.complie(pair);
        NfaIntepretor nfaIntepretor1 = new NfaIntepretor(pair.startNode, "6545qq.com");
        String o = nfaIntepretor1.match();
        assert o.equals("6545qq.com");
    }

    /**
     * test sub method
     *
     * @throws Exception
     */
    @Test
    public void test_sub_method() throws Exception {
        lexer = new Lexer("[1-9]*qq.[a-z]*");
        nfaMachineConstructor = new NfaMachineConstructor(lexer);
        nfaMachineConstructor.complie(pair);
        NfaIntepretor nfaIntepretor1 = new NfaIntepretor(pair.startNode, "6545qq.comabcdefg999");
        String sub = nfaIntepretor1.sub("11111");
        System.out.println(sub);
        assert "11111999".equals(sub);
    }


    /**
     * test
     *
     * @param args
     * @throws Exception
     */




}
