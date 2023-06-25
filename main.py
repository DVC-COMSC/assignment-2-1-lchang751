def main():
    """
    ##################################################
    # Complete your code here
    Use the same variables: m_perc f_perc
    ##################################################
    """
    males=int(input("Enter number of males: "))
    females=int(input("Enter number of females: "))
    total=males+females
    m_perc=(males/total)*100
    f_perc=(females/total)*100

    print(total)
    print(males)
    print(females)
    print (f'Percent males \t {m_perc:.2f}')
    print (f'Percent females \t {f_perc:.2f}')
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
