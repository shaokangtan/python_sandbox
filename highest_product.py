# time(O) = nlogog(n)

def highest_product(list_of_ints):
    if len(list_of_ints) < 3:
        return None
    sorted_ints = sorted(list_of_ints)
    return max(sorted_ints[0] * sorted_ints[1] * sorted_ints[-1], sorted_ints[-3] * sorted_ints[-2] * sorted_ints[-1])

#time(O) = n
def highest_product_of_3(list_of_ints):
    highest = max(list_of_ints[:2]);
    lowest = min(list_of_ints[:2]);

    highestProductOf2 = list_of_ints[0]*list_of_ints[1];
    lowestProductOf2 = list_of_ints[0]*list_of_ints[1];

    highestProductOf3 = list_of_ints[0]*list_of_ints[1]*list_of_ints[2];

    for i in range( i =2, len(list_of_ints) ):
        int current = list_of_ints[i];

        #Max of 3 values:
        ##                  highest_product_of_3            OR
        ##                  current*highestProductOf2       OR
                                                                                                                //                  current*lowestProductOf2

        highestProductOf3 = max(max(highestProductOf3, current * highestProductOf2),
                                current*lowestProductOf2);

        highestProductOf2 = max(max(highestProductOf2, current * highest),
                                current*lowest);

        lowestProductOf2 = min(min(lowestProductOf2, current*highest),
                               current*lowest);

        highest = max(highest, current)      // update highest

        lowest = min(lowest, current)          // update lowest



    return highestProductOf3;


'''
#define size 5
int A[size] = {5,4,5,10,-6};

int highest_product_of_3()
{
    int highest = max(A[0],A[1]);
    int lowest = min(A[0],A[1]);

    int highestProductOf2 = A[0]*A[1];
    int lowestProductOf2 = A[0]*A[1];

    int highestProductOf3 = A[0]*A[1]*A[2];

    for (int i=2;i<size;i++)
    {
        int current = A[i];

        // Max of 3 values:
        //                  highest_product_of_3            OR
        //                  current*highestProductOf2       OR
        //                  current*lowestProductOf2

        highestProductOf3 = max(max(highestProductOf3, current*highestProductOf2),
                                current*lowestProductOf2);

        highestProductOf2 = max(max(highestProductOf2, current*highest),
                                current*lowest);

        lowestProductOf2 = min(min(lowestProductOf2, current*highest),
                                current*lowest);

        highest = max(highest, current);        // update highest

        lowest = min(lowest, current);          // update lowest
    }


    return highestProductOf3;
}
'''