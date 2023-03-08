import numpy as np 
import scipy.stats as stats

'''''''''''''''''''1.标准正态分布'''''''''''''''''''
#loc:均值, scale:标准差
def normal_samples(size):
    return np.random.normal(0, 1, size)


'''''''''''''''''''2.韦伯分布'''''''''''''''''''
#产生具有a个标准差的韦伯分布
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
#loc:均值, scale:标准差
def normal_samples(loc, scale, size):
    return np.random.normal(loc, scale, size)

'''''''''''''''''''8.卡方分布'''''''''''''''''''
#df:自由度
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
#分布的形状 必须为正
def pareto_samples(a, size):
    return np.random.pareto(a, size)

'''''''''''''''''''13.几何分布'''''''''''''''''''
def geometric_samples(p, size):
    return np.random.geometric(p, size)

'''''''''''''''''''14.超几何分布'''''''''''''''''''
#ngood:样本总数中属于“有效”类别的样本数 nbad：样本总数中属于“无效”类别的样本数 nsample：抽样数
def hypergeometric_samples(ngood, nbad, nsample, size):
    return np.random.hypergeometric(ngood, nbad, nsample, size)

'''''''''''''''''''15.二项分布'''''''''''''''''''
#n：抛掷次数，p：成功概率
def binomial_samples(n, p, size):
    return np.random.binomial(n,p,size)

'''''''''''''''''''16.泊松分布'''''''''''''''''''
def poisson_samples(scale, size):
    return np.random.poisson(scale, size)

'''''''''''''''''''17.伽马分布'''''''''''''''''''
#shape：表示伽马分布的形状参数 scale：表示伽马分布的尺度参数 非负
def gamma_samples(shape, scale, size):
    return np.random.gamma(shape, scale,size)

'''''''''''''''''''18.帕斯卡分布'''''''''''''''''''
#k：次数参数 p：概率参数
def pascal_samples(k, p, size):
    return np.random.negative_binomial(k, p, size)

'''''''''''''''''''19.三角分布'''''''''''''''''''
#left,mode,right：三角形分布的左、中、右顶点
def triangular_samples(left, mode, right, size):
    return np.random.triangular(left, mode, right, size)

'''''''''''''''''''20.Levy分布'''''''''''''''''''
def levy_samples(alpha, beta, size):
    return stats.levy_stable.rvs(alpha=alpha, beta=beta, size=size)
print(levy_samples(1.5,0.5,100))