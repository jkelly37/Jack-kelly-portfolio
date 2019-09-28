public class FloorPlan{
    private Rectangle[] squarelist;
    public FloorPlan(Rectangle[] rec){
        squarelist =  new Rectangle[rec.length];
        squarelist =  rec;

        //System.out.print(squarelist[1]);

    }
    public int getArea(){
        int i = 0;
        int area = 0;

        while (i< squarelist.length){
            area = squarelist[i].getArea() + area;
            //System.out.print(squarelist[i].getArea());
            i = i+1;
        }
        return area;



    }
/*
    public int getNumber(){
        return this.squarelist.length;
    }

*/

}
