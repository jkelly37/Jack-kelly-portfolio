import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

// since this one orders the tree randomly it might be worth testing it repeatedly to make sure there's no word order that breaks your algorithm
public class WordCountTreeTest {

    // Special syntax for arbitrary numbers of arguments. secretly the parameters are just packed into an array.
    public static List<String> randomOrderWordList(WordCount ... words) {
        ArrayList<String> output = new ArrayList<>();
        for(WordCount word : words) {
            for(int i = 0; i < word.getCount(); i++) {
                output.add(word.getWord());
            }
        }
        Collections.shuffle(output);
        return output;
    }

    public static void main(String[] args) {
        List<String> words = randomOrderWordList(new WordCount("a",10),
                                                 new WordCount("b", 31),
                                                 new WordCount("c", 2),
                                                 new WordCount("d", 5));
        WordCountTree wct = new WordCountTree();
        for(String word : words) {
            wct.count(word);
        }

        System.out.println(wct.getUniqueWordCount()); // 4
        System.out.println(wct.getTotalWordCount());  // 48
        System.out.println(wct.contains("a"));        // true
        System.out.println(wct.contains("b"));        // true
        System.out.println(wct.contains("c"));        // true
        System.out.println(wct.contains("d"));        // true
        System.out.println(wct.contains("e"));        // false
        System.out.println(wct.contains("f"));        // false
        System.out.println(wct.getCount("a"));        // 10
        System.out.println(wct.getCount("b"));        // 31
        System.out.println(wct.getCount("c"));        // 2
        System.out.println(wct.getCount("d"));        // 5
        System.out.println(wct.getCount("e"));        // 0
        System.out.println(wct.getCount("f"));        // 0

        List<WordCount> wordsInOrder = wct.wordsInOrder();
        System.out.println(wordsInOrder.size());      // 4
        for(WordCount wc : wordsInOrder) {
            System.out.println(wc);
        }
        // b (31)
        // a (10)
        // d (5)
        // c (2)
    }
}

/*
Expected output:

4
48
true
true
true
true
false
false
10
31
2
5
0
0
4
b (31)
a (10)
d (5)
c (2)

 */