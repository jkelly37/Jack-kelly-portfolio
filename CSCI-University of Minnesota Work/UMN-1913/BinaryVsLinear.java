class BinaryVsLinear
{

//Checks each individual element to see if equal to key
  private static int linearSearch(int key, int[] array){
    int comp = 0;
    int i =0;
    while (i< array.length){
      comp++;
      if(array[i] == key){

        return comp;
      }
      i++;

    }
    return comp;
  }


//checks if value is in first or second half of list,
// selects segement it is in and divides that segment
// into two and repeats
  private static int binarySearch(int key, int[] array)
  {
    int comp = 0;
    int low = 0;
    int mid = 0;
    int high = array.length-1;
    while (low<high){
      mid = (low+high)/2;
      comp++;
      if (key == array[mid]){

        return comp;
      }

      else if (key> array[mid]){
        comp++;
        low = mid + 1;
      }
      else{
        comp++;
        high = mid - 1;
      }


    }
    return comp;



  }



  public static void main(String[] args)
  {
    for (int length = 1; length <= 40; length += 1)
    {
      int[] array = new int[length];
      for (int index = 0; index < length; index += 1)
      {
        array[index] = index;
      }

      double linearTotal = 0.0;
      double binaryTotal = 0.0;
      for (int element = 0; element < length; element += 1)
      {
        linearTotal += linearSearch(element, array);
        binaryTotal += binarySearch(element, array);
      }

      double linearAverage = linearTotal / length;
      double binaryAverage = binaryTotal / length;
      System.out.println(length + " " + linearAverage + " " + binaryAverage);
    }
  }
}
