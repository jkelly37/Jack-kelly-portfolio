import java.util.List;
import java.awt.Color;
import java.util.Random;

public class BookStats {

    public static WordCountTree readBook(String fileName, WordCountTree ignoreWords){
        long start = System.currentTimeMillis();
        WordCountTree tree = new WordCountTree();
        WordIterator iterator = new WordIterator(fileName);
        while(iterator.hasNext()){
            String temp = iterator.next();
            if(ignoreWords!=null) {
                if (!ignoreWords.contains(temp)) {
                    tree.count(iterator.next());
                }
            }
            else{
                tree.count(iterator.next());
            }
        }
        System.out.println("Read "+ fileName + " in " + (System.currentTimeMillis()-start) + "ms");
        return tree;
    }

    public static void summarize(WordCountTree wc){
        List<WordCount> top = wc.wordsInOrder();
        int i = 0;
        while(i<25){
            System.out.println(top.get(i).toString());
            i++;
        }
    }

    public static void render(WordCountTree wc, int max_words){
        Random rand = new Random();
        WordlGenerator cloud = new WordlGenerator(2500,2500);
        cloud.setCountRange(max_words,max_words/2);
        cloud.setSpeedMult(5);
        cloud.setFontRange(45,230);
        int i =0;
        List<WordCount> words = wc.wordsInOrder();
        //System.out.println(words.size());
        words=words.subList(0,max_words+1);

        while (i<max_words){
            float r = rand.nextFloat();

            float g = rand.nextFloat();

            float b = rand.nextFloat();

            Color col = new Color(r, g, b);
            cloud.setColor(col);
            cloud.addWord(words.get(i));
            i++;
        }
        cloud.save("test.png");
    }

    public static void main(String[] args){
        WordCountTree t = readBook("StopWords.txt",null);
        WordCountTree book = readBook("TheWooingOfWistaria.txt", t);
        //System.out.println(book.wordsInOrder());
        summarize(book);
        render(book,200);

    }

}
