import java.util.HashSet;
import java.util.Iterator;
import java.util.Set;
import java.util.Stack;


public class NfaIntepretor {
    private Nfa start;
    private String str;

    public NfaIntepretor(Nfa start, String string) {
        this.start = start;
        this.str = string;
    }


    private Set<Nfa> e_closure(Set<Nfa> input) {
        /*
         * 计算input集合中nfa节点所对应的ε闭包，
         * 并将闭包的节点加入到input中
         */
        System.out.print("ε-Closure( " + strFromNfaSet(input) + " ) = ");

        Stack<Nfa> nfaStack = new Stack<Nfa>();
        if (input.isEmpty()) {
            return null;
        }

        nfaStack.addAll(input);

        while (!nfaStack.empty()) {

            Nfa p = nfaStack.pop();

            if (p.next != null && p.getEdge() == Nfa.EPSILON) {

                if (!input.contains(p.next)) {
                    nfaStack.push(p.next);
                    input.add(p.next);
                }
            }

            if (p.next2 != null && p.getEdge() == Nfa.EPSILON) {

                if (!input.contains(p.next2)) {
                    nfaStack.push(p.next2);
                    input.add(p.next2);
                }
            }
        }
        System.out.println("{ " + strFromNfaSet(input) + " }");
        return input;
    }

    private String strFromNfaSet(Set<Nfa> input) {
        StringBuilder s = new StringBuilder();

        Iterator it = input.iterator();
        while (it.hasNext()) {
            s.append(((Nfa) it.next()).getStateNum());
            if (it.hasNext()) {
                s.append(",");
            }
        }

        return s.toString();
    }

    private Set<Nfa> move(Set<Nfa> input, char c) {

        Set<Nfa> outSet = new HashSet<Nfa>();

        for (Nfa p : input) {
            Byte cb = (byte) c;
            if (p.getEdge() == c || (p.getEdge() == Nfa.CCL && p.inputSet.contains(cb))) {
                outSet.add(p.next);
            }
        }
        if (!outSet.isEmpty()) {
            System.out.print("move({ " + strFromNfaSet(input) + " }, '" + c + "')= ");
            System.out.println("{ " + strFromNfaSet(outSet) + " }");
        }

        return outSet;
    }

    void match() {
        //从控制台读入要解读的字符串

        Set<Nfa> next = new HashSet<Nfa>();
        next.add(start);
        e_closure(next);

        Set<Nfa> current;

        StringBuilder inputStr = new StringBuilder();
        char ch;
        for (int i = 0; i < str.length(); i++) {
            current = move(next, (ch = str.charAt(i)));
            next = e_closure(current);
            if (next == null) {
                break;
            }
            inputStr.append(ch);
        }
        System.out.println("The Nfa Machine can recognize string: " + inputStr);
    }

    private boolean hasAcceptState(Set<Nfa> input) {
        boolean isAccepted = false;
        if (input == null || input.isEmpty()) {
            return false;
        }
        StringBuilder acceptedStatement = new StringBuilder("Accept State: ");
        for (Nfa p : input) {
            if (p.next == null && p.next2 == null) {
                isAccepted = true;
                acceptedStatement.append(p.getStateNum()).append(" ");
            }
        }
        if (isAccepted) {
            System.out.println(acceptedStatement.toString());
        }
        return isAccepted;
    }
}

