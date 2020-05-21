import com.sun.deploy.util.StringUtils;

import java.util.ArrayList;
import java.util.List;

/**
 * @author author
 */
public class NfaPrinter {
    private static final int ASCII_NUM = 128;
    private boolean start = true;

    public void printNfa(Nfa startNfa) {
        if (startNfa == null || startNfa.isVisited()) {
            return;
        }
        if (start){
            System.out.println("digraph G { \nrankdir=LR;");
            start=false;
        }

        startNfa.setVisited();

        printNfaNode(startNfa);


        printNfa(startNfa.next);
        printNfa(startNfa.next2);
    }

    private void printNfaNode(Nfa node) {
        if (node.next == null) {
            System.out.print(" }");
        } else {
            System.out.print(String.format("%s -> %s %s", node.getStateNum(), node.next.getStateNum(), getEdgeString(node)));
            System.out.print("\n");
            if (node.next2 != null) {
                System.out.print(String.format("%s -> %s %s", node.getStateNum(), node.next2.getStateNum(), getEdgeString(node)));
                System.out.print("\n");
            }
        }
    }

    private String getEdgeString(Nfa node) {
        String res = "";
        switch (node.getEdge()) {
            case Nfa.CCL:
                res = "[label=\"CLL\"];";
                break;
            case Nfa.EPSILON:
                res = "[label=\"EPSILON\"];";
                break;

            default:
                res =" [label=\"" + (char) node.getEdge() + "\"];";
                break;
        }
        return res;
    }
}
