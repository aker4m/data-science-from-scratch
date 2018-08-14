from probability import normal_cdf, inverse_normal_cdf
import math, random

def normal_approximation_to_binomial(n, p):
    """finds mu and sigma corresponding to a Binomial(n, p)"""
    mu = p * n
    sigma = math.sqrt(p * (1 - p) * n)
    return mu, sigma

#probabilities a normal lies in an interval

normal_probability_below = normal_cdf

def normal_probability_above(lo, mu=0, sigma=1):
    return 1 - normal_cdf(lo, mu, sigma)

def normal_probability_between(lo, hi, mu=0, sigma=1):
    return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)

def normal_probability_outside(lo, hi, mu=0, sigma=1):
    return 1 - normal_probability_between(lo, hi, mu, sigma)

#normal bounds


if __name__ == '__main__':
    mu_0, sigma_0 = normal_approximation_to_binomial(1000, 0.5)
    print('mu_0', mu_0)
    print('sigma_0', sigma_0)
    print('normal_two_sided_bounds(0.95, mu_0, sigma_0)',
            normal_two_sided_bounds(0.95, mu_0, sigma_0))
    print()
    print('power of a test')

    print('95% bounds based on assumption p is 0.5')

    lo, hi = normal_two_sided_bounds(0.95, mu_0, sigma_0)
    print('lo {}, hi {}'.format(lo, hi))

    print('actual mu and sigma based on p = 0.55')
    mu_1, sigma_1 = normal_approximation_to_binomial(1000, 0.55)
    print('mu_1 {}, sigma_1 {}'.format(mu_1, sigma_1))

    type_2_probability = normal_probability_between(lo, hi, mu_1, sigma_1)
    power = 1 - type_2_probability

    print('type 2 probability', type_2_probability)
    print('power', power)
    print()

    print('one-sided test')
    hi = normal_upper_bound(0.95, mu_0, sigma_0)
    print('hi', hi)
    type_2_probability = normal_probability_below(hi, mu_1, sigma_1)
    power = 1 - type_2_probability
    print('type 2 probability', type_2_probability)
    print('power', power)
    print()

    print('two_sided_p_value(529.5, mu_0, sigma_0)',
            two_sided_p_value(529.5, mu_0, sigma_0))
    print('two_sided_p_value(531.5, mu_0, sigma_0)',
            two_sided_p_value(531.5, mu_0, sigma_0))
    print('upper_p_value(525, mu_0, sigma_0)', 
            upper_p_value(525, mu_0, sigma_0))
    print('upper_p_value(527, mu_0, sigma_0)',
            upper_p_value(527, mu_0, sigma_0))
    print()

    print('P-hacking')

    random.seed(0)
    experiments = [run_experiment() for _ in range(1000)]
    num_rejections = len([experiment for experiment in experiments
                            if reject_fairness(experiment)])
    print(num_rejections, 'rejections out of 1000')
    print()

    print('A/B testing')
    z = a_b_test_statistic(1000, 200, 1000, 180)
    print('a_b_test_statistic(1000, 200, 1000, 180)', z)
    print('p-value', two_sided_p_value(z))
    z = a_b_test_statistic(1000, 200, 1000, 150)
    print('a_b_test_statistic(1000, 200, 1000, 150)', z)
    print('p-value', two_sided_p_value(z))
