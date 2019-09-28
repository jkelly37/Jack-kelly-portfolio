public class Hand {
    private Card[] handCards;
    private int size;
    private Deck deck;
    public Hand(Deck deck, int size){
        handCards = new Card[size];
        this.deck = deck;
        int i = 0;
        this.size = size;
        while(i< size){
            Card card = deck.draw();
            handCards[i] = card;
            i++;
        }

    }


    public int getSize(){
        return size;
    }

    public Card get(int i){
        if (i < 0 || i>size-1) {
            System.out.println("is is "+ i + "but size is "+ getSize());
            throw new IllegalArgumentException();
        }
        return handCards[i];
    }

    public boolean remove(Card card){
        int i = 0;
        if(card==null){
            System.out.println("bruh");
            return false;
        }
        while(i<size){
            if(card.equals(handCards[i])){
                handCards[i]= deck.draw();
                return true;
            }
            i++;
        }
        return false;

    }

    @Override
    public String toString() {
        int i = 0;
        String s = "";
        while (i<handCards.length){
            s = s+ "card in hand" + handCards[i] +"\n";
            i++;
        }
        return s;
    }
}
