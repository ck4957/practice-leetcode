public class ReverseLinkedList {
    public ListNode reverseList(ListNode head) {
        System.out.println("ReverseList invoked");
        ListNode prev = null;
        ListNode curr = head;
        while(curr != null) {
            ListNode nextTemp = curr.next;
            curr.next = prev;
            prev = curr;
            curr= nextTemp;
        }
        return prev;
    }

    public static void main(String args[]) {
        ListNode head = null;
        ReverseLinkedList rLinkedList = new ReverseLinkedList();
        rLinkedList.reverseList(head);
    }
}

class ListNode {
    int val;
    ListNode next;
    ListNode(int x) {
        val = x;
    }
}

