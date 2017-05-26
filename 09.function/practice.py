
('cat')
n range(1,10):
    #         for y1 in range(1,10):
    #             if x1 %2 == 0:
    #                 print('{} * {} = {}'.format(x1,y1,x1*y1))
    #     gugudan()


    def make_dict(list1,list2):
            empty_dict = {}
                for x1,y1 in zip(list1,list2):
                            empty_dict[x1] = y1
                                    return empty_dict

                                print(make_dict('a b c d'.split(),'1 2 3 4'.split()))

