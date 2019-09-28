public class Triangle extends Polygon {

    public Triangle(int side1, int side2, int side3){

        super(3,side1,side2,side3);

        if (side1 + side3< side2){
            throw new RuntimeException();
        }
        if (side2 + side3 < side1){
            throw new RuntimeException();
        }
        if (side2 + side1 < side3){
            throw new RuntimeException();
        }



    }

}
