import java.util.Random;
public class UnoWarMatch {
    private AI ai1;
    private AI ai2;

    public UnoWarMatch(AI ai1, AI ai2) {
        this.ai1 = ai1;
        this.ai2 = ai2;

    }

    public boolean playGame() {
        int p1Score = 0;
        int p2Score = 0;
        int winner = 1;

        Deck deck = new Deck();
        Hand hand1 = new Hand(deck, 5);
        Hand hand2 = new Hand(deck, 5);
        while ((p1Score < 10) && (p2Score < 10)) {
            CardPile cardPile = new CardPile(deck.draw());
            Player player1 = new Player(ai1, hand1, cardPile,1);
            Player player2 = new Player(ai2, hand2, cardPile,2);
            if (winner==1) {
                //System.out.println("so yeah");
                winner = playTurn(player1, player2, cardPile, deck);
                if(winner==1){p1Score++;}
                else{p2Score++;}
            } else if (winner==2) {
                //System.out.println("death");
                winner = playTurn(player2, player1, cardPile, deck);
                if(winner==2){p2Score++;}
                else{p1Score++;}
            }
            //System.out.println("winnter is " + winner);
        }
        return p1Score>9;
    }


    public int playTurn(Player player1, Player player2, CardPile cardPile, Deck deck){
        Card card1 = player1.playCard();

        if (card1==null){
            return player2.getId();
        }
        else{
            Card card2 = player2.playCard();
            if(card2==null){
                player1.incScore();
                return player1.getId();
            }
           return playTurn(player1,player2,cardPile,deck);
        }
    }


    public double winRate(int nTrials) {
        int i=0;
        double ai1Wins = 0.0;
        while(i<nTrials){
            if(playGame()){
                //System.out.println("got here tho");
                ai1Wins++;
            }
            i++;
        }
        return ai1Wins/(nTrials*1.0);

    }

}


