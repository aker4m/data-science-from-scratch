

if __name__ == '__main__':
    print('num_points : {}'.format(len(num_friends)))
    print('largest value : {}'.format( max(num_friends) ))
    print('smallest value : {}'.format(min(num_friends)))
    print('second_samllest_value : {}'.format(sorted_values[1]))
    print('second_largest_value : {}'.format(sorted_values[-2]))
    print('mean(num_friends) : {}'.format(mean(num_friends)))
    print('median(num_friends) : {}'.format(median(num_firends)))
    print('quantile(num_friends, 0.10) : {}'.format(quantile(num_friends, 0.10)))
    print('quantile(num_friends, 0.25) : {}'.format(quantile(num_friends, 0.25)))
    print('quantile(num_friends, 0.75) : {}'.format(quantile(num_friends, 0.75)))
    print('quantile(num_friends, 0.90) : {}'.format(quantile(num_friends, 0.90)))

