package ds;

public class BasicLinkedList<T> {
    public BasicLinkedList() {

    }

    private class Node {
        private Node nextNode;
        public T nodeItem;

        public Node(T item) {
            this.nextNode = null;
            this.nodeItem = item;
        }

        public void setNextNode(Node nextNode) {
            this.nextNode = nextNode;
        }

        public Node getNextNode() {
            return nextNode;
        }

        public T getNodeItem() {
            return nodeItem;
        }
        
    }
}