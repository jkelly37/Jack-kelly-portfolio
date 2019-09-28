public class Tournament {
    public static void main(String[] args) {
        AI[] players = new AI[4];
        players =new AI[] {new RandomCardAI(),new SmallestCardAI(),new BiggestCardAI()};
        int i =0;
        while(i<3){
            int j = 0;
            while (j<3){
                UnoWarMatch game13 = new UnoWarMatch(players[i],players[j]);
                System.out.println(players[i].toString() +" vs. " + players[j].toString() +"winRate: "+ (double)Math.round(game13.winRate(100000)*10000)/10000);
                j++;
            }
            i++;
        }

    }
}
