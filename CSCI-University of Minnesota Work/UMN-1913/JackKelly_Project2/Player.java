public class Player {
    private AI ai;
    private Hand hand;
    private int score;
    private CardPile cardPile;
    private int id;

    public Player(AI ai, Hand hand, CardPile cardPile,int id){
        this.ai = ai;
        this.hand=hand;
        this.score=0;
        this.cardPile = cardPile;
        this.id = id;


    }
    public void incScore(){
        this.score++;
    }
    public AI getAi(){
        return this.ai;
    }
    public Card playCard(){
         Card card1 = ai.getPlay(hand,cardPile);
         if(card1!=null){
             hand.remove(card1);
             cardPile.play(card1);
         }
         return card1;
    }

    public Hand getHand(){
        return hand;
    }
    public void updateCardPile(CardPile cardPile){
        this.cardPile=cardPile;
    }
    public int getScore(){
        return score;
    }
    public void setHand(Hand hand){
        this.hand=hand;
    }
    public int getId(){
        return id;
    }
}
