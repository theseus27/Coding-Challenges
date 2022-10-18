import java.util.*;
import java.util.stream.*;

//To allocate memory to an object, you have to use new. Otherwise, only a reference is created.
//Indexing: The index you specify will be the index of the first element you insert...so to insert  at the end, you would use list.size(), NOT list.size()-1.


public class Lists {
    public static void main(String[] args) {
    //CONSTRUCT LIST
        //Arrays.asList() w/ list of elts.
        List<Integer> testlist = new ArrayList<Integer>(Arrays.asList(1, 2, 3));

        //Arrays.asList() w/ existing array
        Integer[] nums = new Integer[] {4, 5, 6};
        List<Integer> testlist2 = new ArrayList<Integer>(Arrays.asList(nums));

        //List.of() 
        //          ***IMMUTABLE***
        List<Integer> testlist3 = List.of(6, 7, 8);

        //Use another Collection    
        //          ***Is it's own copy, changes to original won't affect this***
        List<Integer> testlist4 = new ArrayList<Integer>(testlist);

        //STREAM
        Stream<Integer> s = Stream.of(10, 12, 14);
        List<Integer> testlist5 = new ArrayList<Integer>(s.collect(Collectors.toList()));
        //OR
        //List<Integer> testlist6 = s.collect(Collectors.toCollection(ArrayList::new));

    //ADDING ELEMENTS
        //list.add(val)    ***Adds to end of list***
        testlist.add(4);

        //list.add(idx, val)
        testlist.add(3, 10);

        //list.addAll(Collection)
        testlist.addAll(testlist3);

        //list.addAll(idx, Collection)
        testlist4.addAll(testlist4.size(), testlist5);

    //REMOVE ELEMENTS
        //remove(idx)   ***Takes precedent over remove(val)
        testlist.remove(2);

        //remove(val)
        //testlist4.remove(new Integer(12));


        testlist = testlist.subList(1, testlist.size());

        System.out.println(testlist);
        System.out.println(testlist4);

    //OTHER
        //set
        testlist4.set(0, 21);

        //get
        System.out.println(testlist4.get(0));

        //clear
        testlist5.clear();

        //contains
        System.out.println(testlist4.contains(12));
        
        //hashCode
        System.out.println(testlist.hashCode());

        //indexOf   ***Return index of first occurence or -1***
        System.out.println(testlist.indexOf(20));

        //max/min
        System.out.println(Collections.min(testlist));
    }
}