public class SmallestCardAI implements AI {
    @Override
    public Card getPlay(Hand hand, CardPile cardPile) {
        int size = hand.getSize();
        int i = 0;
        int smallestIndex=-1;
        int smallestValue=100;
        int topcardValue = cardPile.getTopCard().getRankNum();
        while(i<size) {
            if((cardPile.canPlay(hand.get(i))) && hand.get(i).getRankNum()<smallestValue){
                smallestIndex=i;
                smallestValue = hand.get(i).getRankNum();

            }
            i++;

        }
        if(smallestIndex==-1){
            return null;
        }

        return hand.get(smallestIndex);


    }



    public String toString() {
        return "Smallest Card AI";
    }
}
