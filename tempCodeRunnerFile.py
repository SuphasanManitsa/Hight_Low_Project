plt.figure(figsize = (12,12))
# for i in range(9):
#     plt.subplot(3,3,i + 1)
#     x_one = np.ones(100)
#     x_zero = np.zeros(100)
#     o = []
#     z = []
#     for j,k in zip(x_one,x_zero):
#         o.append(hl.hight_low(balance = balance,hit = 1,n = 10000,re = 1,a = j))
#         z.append(hl.hight_low(balance = balance,hit = 1,n = 10000,re = 1,a = k))
#     plt.plot(x_one,o)
#     plt.plot(x_zero,z)
#     plt.title(f'Round {i + 1}')
# plt.show()