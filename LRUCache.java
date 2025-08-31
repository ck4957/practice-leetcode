import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL; 
import org.json.JSONObject;
public class LRUCache {
    private class Node {
        private int key;
        private int value;
        Node prev, next;

        Node(int k, int v) {
            this.key = k;
            this.value = v;
        }
        Node() {
            this(0, 0);
        }
    }
    private int capacity, count;
    private Map<Integer, Node> map;
    private Node head, tail;
    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.count = 0;
        map = new HashMap<>();
        head = new Node();
        tail = new Node();
        head.next = tail;
        tail.prev = head;
        
    }
    
    public int get(int key) {
        Node n = map.get(key);
        if (n == null) {
            return -1;
        }
        update(n);
        return n.value;
    }
    
    public void put(int key, int value) {
        Node n = map.get(key);
        if (n == null) {
            n = new Node(key, value);
            map.put(key, n);
            add(n);
            ++count;
        } else {
            n.value = value;
            update(n);
        }
        if (count > capacity) {
            Node toDel = tail.prev;
            remove(toDel);
            map.remove(toDel.key);
            --count;
        }
    }

    public void remove(Node node) {
        Node before = node.prev, after = node.next;
        before.next = after;
        after.prev = before;
    }

    public void add(Node node) {
        Node after = head.next;
        head.next = node;
        node.prev = head;
        node.next = after;
        after.prev = node;
    }

    private void update(Node n) {
        remove(n);
        add(n);
    }

    void printMap() {
        System.out.println("-----Printing Map-------");
        for (Map.Entry<Integer, Node> entry : map.entrySet()) {
            System.out.println(entry.getKey()+" : "+entry.getValue().value);
        }
    }

    class Result {
        private int page;
        @SerializedName("per_page")
        int perPage;
        int total;
        @SerializedName("total_pages")
        int totalPages;
        Data[] data;
    }

    class Data {
        String poster;
        String type;
        int year;
        String imdbId;
    }

    getMovies() {
        Result staff = gson.fromJson(reader, Result.class);
    }

    static void getNumberOfMovies(String movie) {
        String url = "https://jsonmock.hackerrank.com/api/movies/search/?Title=" + movie;
     URL obj = new URL(url);
     HttpURLConnection con = (HttpURLConnection) obj.openConnection();
     // optional default is GET
     con.setRequestMethod("GET");
     //add request header
     con.setRequestProperty("User-Agent", "Mozilla/5.0");
     int responseCode = con.getResponseCode();
     System.out.println("\nSending 'GET' request to URL : " + url);
     System.out.println("Response Code : " + responseCode);
     BufferedReader in = new BufferedReader(
             new InputStreamReader(con.getInputStream()));
     String inputLine;
     StringBuffer response = new StringBuffer();
     while ((inputLine = in.readLine()) != null) {
     	response.append(inputLine);
     }
     in.close();
     //print in String
     System.out.println(response.toString());
     //Read JSON response and print
     JSONObject myResponse = new JSONObject(response.toString());
     System.out.println("result after Reading JSON Response");
     System.out.println("total- "+myResponse.getString("total"));
   
    }


    public static void main(String[] args) {
		LRUCache lRUCache = new LRUCache(2);
        lRUCache.put(1, 1); // cache is {1=1}
        lRUCache.printMap();
        lRUCache.put(2, 2); // cache is {1=1, 2=2}
        lRUCache.printMap();
        lRUCache.get(1);    // return 1
        lRUCache.printMap();
        lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
        lRUCache.get(2);    // returns -1 (not found)
        lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
        lRUCache.get(1);    // return -1 (not found)
        lRUCache.get(3);    // return 3
        lRUCache.get(4);    // return 4
        lRUCache.printMap();
        main2();
	}
}