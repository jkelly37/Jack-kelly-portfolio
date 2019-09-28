import java.util.LinkedList;
import java.util.List;
public class WordCountTree {
    private WordBSTNode root;
    private int totalWordCount;
    private int uniqueWordCount;

    private LinkedList<WordCount> wordList=new LinkedList<>();

    public WordCountTree(){
        this.root= new WordBSTNode(null,null,null);
        totalWordCount=0;
    }

    public void count(String word){
        if (root.data==null){
            uniqueWordCount++;
            totalWordCount++;
            root.setData(new WordCount(word,1));
        }
        else {
            boolean add1 = !contains(word);
            if (!add1) {
                WordCount newadd = search(word, root);
                newadd.addCount();
                totalWordCount++;
            } else {
                addword(word, root);
                totalWordCount++;
                uniqueWordCount++;
            }
        }
    }

    public int getCount(String word){
        WordCount count = search(word,root);
        if(count!=null){
            return count.getCount();
        }
        return 0;
    }
    public boolean contains(String word){
        return containshelper(word,root);
    }

    public void addword(String word, WordBSTNode tree){
        if(tree==null){
            tree = new WordBSTNode(new WordCount(word,1),null,null);
            //System.out.println("uh oh");
        }
        else if(word.compareTo(tree.getData().getWord())>0){
            if(tree.getRight()==null){
                tree.setRight(new WordBSTNode(new WordCount(word,1),null,null));
            }
            else {
                addword(word, tree.getRight());
            }
        }
        else if(word.compareTo(tree.getData().getWord())<0){
            if(tree.getLeft()==null){
                tree.setLeft(new WordBSTNode(new WordCount(word,1),null,null));
            }
            else {
                addword(word, tree.getLeft());
            }
        }



    }

    public boolean containshelper(String word,WordBSTNode tree){
        //System.out.println("got word"+word+ "tree word" + tree.getData().getWord());
        if(tree==null){
            return false;
        }
        else if(word.equals(tree.data.getWord())){
            return true;
        }
        else if(word.compareTo(tree.getData().getWord())>0){
            return containshelper(word,tree.getRight());
        }
        else if(word.compareTo(tree.getData().getWord())<0){
            return containshelper(word,tree.getLeft());
        }
        return false;

    }

    public int getTotalWordCount(){
        return totalWordCount;
    }

    public int getUniqueWordCount(){
        return uniqueWordCount;
    }

    public List<WordCount> wordsInOrder(){
        LinkedList<WordCount> nodeList = new LinkedList<>();
        wordsInOrderHelper(root, nodeList);
        nodeList.sort(WordCount::compareTo);
        return nodeList;
    }

    public void wordsInOrderHelper(WordBSTNode tree, LinkedList<WordCount> nodeList){
        if(tree!=null){
            wordsInOrderHelper(tree.getLeft(),nodeList);
            nodeList.add(tree.getData());
            wordsInOrderHelper(tree.getRight(),nodeList);

        }
    }


    public WordCount search(String word, WordBSTNode tree){
        if(tree==null){
            return null;
        }
        if(tree.getData().getWord().equals(word)){
            return tree.getData();
        }
        else if(word.compareTo(tree.getData().getWord())>0){
            return search(word,tree.getRight());
        }
        else if(word.compareTo(tree.getData().getWord())<0){
            return search(word,tree.getLeft());
        }
        return null;

    }

    private class WordBSTNode{
        private WordCount data;
        private WordBSTNode left;
        private WordBSTNode right;
        private WordBSTNode(WordCount data, WordBSTNode left, WordBSTNode right){
            this.data=data;
            this.left=left;
            this.right=right;
        }

        public WordCount getData() {
            return data;
        }

        public WordBSTNode getLeft() {
            return left;
        }

        public WordBSTNode getRight() {
            return right;
        }

        public void setData(WordCount data) {
            this.data = data;
        }

        public void setLeft(WordBSTNode left) {
            this.left = left;
        }

        public void setRight(WordBSTNode right) {
            this.right = right;
        }
    }



}
