public class WordCount implements Comparable<WordCount>{
    private String word;
    public int count = 0;
    public WordCount(String word, int count) {
        this.word=word;
        this.count=count;

    }
    public WordCount(String word){
         new WordCount(word,1);
    }
    public String getWord(){
        return word;
    }

    public int getCount(){
        return this.count;
    }
    public void addCount(){
        count++;
    }

    @Override
    public String toString() {
        return this.word + " (" +count+")";
    }

    @Override
    public int compareTo(WordCount o) {
        if(count==o.getCount()){
            return 0;
        }
        else if (count>o.getCount()){
            return -1;
        }
        else {
            return 1;
        }

    }
}
