import java.util.Random;
public class RandomCardAI implements AI{
    @Override
    public Card getPlay(Hand hand, CardPile cardPile) {
        int i=0;
        int size = hand.getSize();
        while(i<size){
            if(cardPile.canPlay(hand.get(i))){
                return hand.get(i);
            }
            i++;

        }
        return null;

    }

    public String toString() {
        return "Random Card AI";
    }
}
