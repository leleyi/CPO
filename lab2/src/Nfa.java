import java.util.HashSet;
import java.util.Iterator;
import java.util.Set;

public class Nfa {

    public enum ANCHOR {
        NONE,
        START,
        END,
        BOTH
    }

    //边对应的是ε
    public static final int EPSILON = -1;
    //边对应的是字符集
    public static final int CCL = -2;
    //该节点没有出去的边
    public static final int EMPTY = -3;

    //边对应 有数量的{}
    public static final int BOUND = -4;


    private static final int ASCII_COUNT = 127;

    //记录转换边对应的输入，输入可以是空, ε，字符集(CCL),或空，也就是没有出去的边
    private int edge;

    public int getEdge() {
        return edge;
    }

    public void setEdge(int type) {
        edge = type;
    }
//    public void setConstrain(int min, int max){
//        edge = this.BOUND;
//    }

    //用来存储字符集类
    public Set<Byte> inputSet;

    //跳转的下一个状态，可以是空
    public Nfa next;
    //跳转的另一个状态，当状态含有两条ε边时，这个指针才有效
    public Nfa next2;

    //对应的正则表达式是否开头含有^, 或结尾含有$,  或两种情况都有
    private ANCHOR anchor;

    //节点编号
    private int stateNum;

    //节点是否被访问过，用于节点打印
    private boolean visited = false;

    public void setVisited() {
        visited = true;
    }

    public boolean isVisited() {
        return visited;
    }


    public Nfa() {
        inputSet = new HashSet<Byte>();
        clearState();
    }

    public void setStateNum(int num) {
        stateNum = num;
    }

    public int getStateNum() {
        return stateNum;
    }

    public void addToSet(Byte b) {
        inputSet.add(b);
    }

    public void setComplement() {

        Set<Byte> newSet = new HashSet<Byte>();
        for (byte b = 0; b < ASCII_COUNT; b++) {
            if (inputSet.contains(b) == false) {
                newSet.add(b);
            }
        }

        inputSet = null;
        inputSet = newSet;
    }


    public void setAnchor(ANCHOR anchor) {
        this.anchor = anchor;
    }

    public Nfa.ANCHOR getAnchor() {
        return this.anchor;
    }

    public void clearState() {
        inputSet.clear();
        next = next2 = null;
        anchor = ANCHOR.NONE;
        stateNum = -1;
    }

    public void cloneNfa(Nfa nfa) {
        inputSet.clear();
        Iterator<Byte> it = nfa.inputSet.iterator();
        while (it.hasNext()) {
            inputSet.add(it.next());
        }

        anchor = nfa.getAnchor();
        this.next = nfa.next;
        this.next2 = nfa.next2;
        this.edge = nfa.getEdge();
    }

    @Override
    public boolean equals(Object obj) {
        return super.equals(obj);
    }

    @Override
    public int hashCode() {
        return super.hashCode();
    }
}
