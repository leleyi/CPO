
public class ErrorHandler {
    public enum Error {
        //内存不足
        E_MEM,
        //正则表达式错误
        E_BADEXPR,
        //括号不匹配
        E_PAREN,
        //要解析的正则表达式过多
        E_LENGTH,
        //字符集类没有以 [ 开头
        E_BRACKET,
        //^必须在表达式的开头
        E_BOL,
        //* ? + 后面必须跟着表达式
        E_CLOSE,
        //双引号中不能保护换行符
        E_NEWLINE,
        //没有匹配的 }
        E_BADMAC,
        //给定的宏表达式不存在
        E_NOMAC,
        //宏表达式的间套太深
        E_MACDEPTH
    }

    private static String[] errMsgs = new String[]{
            "Not enough memory for NFA",
            "Malformed regular expression",
            "Missing close parenthesis",
            "Too many regular expression or expression too long",
            "Missing [ in character class",
            "^ must be at the start of expression or after [",
            "+ ? or * must follow an expression or subexpression",
            "Newline in quoted string, use \\n to get newline into expression",
            "Missing ) in macro expansion",
            "Macro deoesn't exist",
            "Macro expansions nested too deeply"
    };

    public static void parseErr(Error type) throws Exception {
        throw new Exception(errMsgs[type.ordinal()]);
    }
}
