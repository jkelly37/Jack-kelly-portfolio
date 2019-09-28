public class BiggestCardAI implements AI {
    @Override
    public Card getPlay(Hand hand, CardPile cardPile) {
        int size = hand.getSize();
        int i = 0;
        int index=-1;
        int bigValue=0;

        while(i<size) {
            Card card = hand.get(i);
            if(cardPile.canPlay(card)){
                if(card.getRankNum()>bigValue){
                    bigValue= card.getRankNum();
                    index=i;
                }
            }
            i++;
        }
        if(index==-1){
            return null;
            //no card to play
        }
        return hand.get(index);


    }

    public String toString() {
        return "Biggest Card AI";
    }
}
