public class Card {
    private int rank;
    private int suit;
    static String[] suitArr = {"Spades", "Hearts", "Clubs", "Diamonds"};
    static String[] rankArr = {"Ace","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack",
    "Queen","King"};
    public Card(int rank, int suit){
        if(rank>0 && suit >0 && rank<14 && suit<5) {
            this.rank = rank;
            this.suit = suit;
        }
        else{
            throw new IllegalArgumentException();
        }

    }
    public int getRankNum(){
        return this.rank;
    }
    public String getRankName(){
        return rankArr[rank-1];
    }
    public String getSuitName(){
        return suitArr[suit-1];

    }

    public String toString(){
        String s = getRankName() + " of " + getSuitName();
        return s;

    }
    public boolean equals(Object obj){
        Card card2 = (Card) obj;
        if(card2.getSuitName() == this.getSuitName() && card2.getRankNum()== this.getRankNum()){
            return true;
        }
        return false;
    }



    }



