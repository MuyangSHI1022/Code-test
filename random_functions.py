import numpy as np 
import scipy.stats as stats

'''''''''''''''''''1.标准正态分布'''''''''''''''''''
def normal_samples(size):
    return np.random.normal(0, 1, size)

'''''''''''''''''''2.韦伯分布'''''''''''''''''''
def weibull_samples(a,size):
    return np.random.weibull(a,size)

'''''''''''''''''''3.指数分布'''''''''''''''''''
#scale: beta
def expoential_samples(scale,size):
    return np.random.exponential(scale, size)

'''''''''''''''''''4.柯西分布'''''''''''''''''''
def cauchy_samples(size):
    return np.random.standard_cauchy(size)

'''''''''''''''''''5.耿贝尔分布'''''''''''''''''''
def gumbel_samples(loc, scale, size):
    return stats.gumbel_r.rvs(loc, scale, size)

'''''''''''''''''''6.beta分布'''''''''''''''''''
def beta_samples(alpha, beta, size):
    return stats.beta.rvs(a=alpha,b=beta,size=size)

'''''''''''''''''''7.服从N(mean,sigama)正态分布'''''''''''''''''''
def normal_samples(loc, scale, size):
    return np.random.normal(loc, scale, size)

'''''''''''''''''''8.卡方分布'''''''''''''''''''
def chi2_samples(df, size):
    return stats.chi2.rvs(df=df, size=size)

'''''''''''''''''''9.F分布'''''''''''''''''''
def f_samples(dfn, dfd, size):
    return stats.f.rvs(dfn=dfn, dfd=dfd, size=size)

'''''''''''''''''''10.学生t分布'''''''''''''''''''
def t_samples(df,size):
    return stats.t.rvs(df=df, size=size)

'''''''''''''''''''11.拉普拉斯分布'''''''''''''''''''
def laplace_samples(loc, scale, size):
    return np.random.laplace(loc, scale, size)

'''''''''''''''''''12.帕累托分布'''''''''''''''''''
def pareto_samples(a, size):
    return np.random.pareto(a, size)

'''''''''''''''''''13.几何分布'''''''''''''''''''
def geometric_samples(p, size):
    return np.random.geometric(p, size)

'''''''''''''''''''14.超几何分布'''''''''''''''''''
def hypergeometric_samples(ngood, nbad, nsample, size):
    return np.random.hypergeometric(ngood, nbad, nsample, size)

'''''''''''''''''''15.二项分布'''''''''''''''''''
def binomial_samples(n, p, size):
    return np.random.binomial(n,p,size)

'''''''''''''''''''16.泊松分布'''''''''''''''''''
def poisson_samples(lam, size):
    return np.random.poisson(lam, size)

'''''''''''''''''''17.伽马分布'''''''''''''''''''
def gamma_samples(shape, scale, size):
    return np.random.gamma(shape, scale,size)

'''''''''''''''''''18.帕斯卡分布'''''''''''''''''''
def pascal_samples(k, p, size):
    return np.random.negative_binomial(k, p, size)

'''''''''''''''''''19.三角分布'''''''''''''''''''
def triangular_samples(left, mode, right, size):
    return np.random.triangular(left, mode, right, size)

'''''''''''''''''''20.Levy分布'''''''''''''''''''
def levy_samples(alpha, beta, size):
    return stats.levy_stable.rvs(alpha=alpha, beta=beta, size=size)

'''''''''''''''''''21.狄拉克分布'''''''''''''''''''
def dirac_samples(mu, kappa, size):
    return np.random.vonmises(mu, kappa, size)

'''''''''''''''''''22.多项式分布'''''''''''''''''''
def polynomial_samples(n, pvals, size):
    return np.random.multinomial(n, pvals, size)

'''''''''''''''''''23.狄利克雷分布'''''''''''''''''''
def dirichlet_samples(alpha, size):
    return np.random.dirichlet(alpha, size)

'''''''''''''''''''24.逻辑斯谛分布'''''''''''''''''''
def logistic_samples(loc, scale, size):
    return np.random.logistic(loc, scale, size)

'''''''''''''''''''25.数据分布'''''''''''''''''''
def choice_samples(vals, pvals, size):
    return np.random.choice(a=vals, p=pvals, size=(size))
