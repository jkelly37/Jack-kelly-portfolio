public class CardPile {
    private Card topCard;
    private int count;

    public CardPile(Card topCard){
        count=1;
        this.topCard = topCard;

    }

    public boolean canPlay(Card card){
        if(card==null){
            return false;
        }
        if(card.getRankNum()>= topCard.getRankNum()|| card.getSuitName().equals(topCard.getSuitName())){
            return true;
        }
        return false;
    }

    public void play(Card card){
        if(canPlay(card)){
            topCard=card;
            count++;
        }
        else{
            throw new IllegalArgumentException();
        }
    }

    public int getNumCards(){
        return count;
    }

    public Card getTopCard(){
        return topCard;
    }



}
