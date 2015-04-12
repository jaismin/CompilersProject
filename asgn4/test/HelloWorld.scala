object sort {
  def sort(a: Array[Int]) : Unit =   {

    def swap(i: Int, j: Int) : Unit = {
      val t: Int = a[i]; 
      a[i] = a[j]; 
      a[j] = t;
    }

    def sort1(l: Int, r: Int): Unit =  {
      val pivot: Int = a[(l+r)/2];
      val i : Int = l;
      val j : Int = r;
      while (i <= j) {
        while (a[i] < pivot)
        {
           i += 1;
        }
        while (a[j] > pivot) 
        {
          j -= 1;
        }
        if (i <= j) {
          swap(i, j);
          i += 1;
          j -= 1;
        }
      }
      if (l < j) {sort1(l, j);}
      if (j < r) {sort1(i, r);}
    }

    // if ( > 0)
    //   sort1(0, a.length - 1)
  }

  // def println(ar: Array[Int]) {
  //   def print1 = {
  //     def iter(i: Int): String =
  //       ar[i] + (if (i < 10) "," + iter(i+1) else "")
  //     // if (ar.length == 0) "" else iter(0)
  //   }
  //   // Console.println("[" + print1 + "]")
  // }

  def main(args: Array[String]) : Unit =  {
    val ar: Array[Int] = Array(6, 2, 8, 5, 1);
    // println(ar)
    sort(ar);
    // println(ar)
  }

}