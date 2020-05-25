import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 6))

y1 = [0.5046040246268209, 0.15363162694655808, 0.12089146531089001, 0.151544046298763, 0.5133452680909094]
x1 = [i / (len(y1) - 1) for i in range(0, len(y1))]
y2 = [0.845018126902458, 0.5194721424281388, 0.3853757542555395, 0.3560832010786681, 0.34439296536384695, 0.3553021092563502, 0.38131362663035223, 0.5036025094020485, 0.830252246751215]
x2 = [i / (len(y2) - 1) for i in range(0, len(y2))]
y3 = [0.8783193875803986, 0.5827294059296804, 0.43912307212594087, 0.40393905639716543, 0.38852811418375716, 0.3851467230959347, 0.3850232188197363, 0.38461226876447996, 0.38595682039846557, 0.40041213288033706, 0.44093438017989417, 0.5801463399957484, 0.8732340732669327]
x3 = [i / (len(y3) - 1) for i in range(0, len(y3))]
y4 = [0.7789395119755115, 0.5627902146090387, 0.8737679675521567, 0.9300906339928109, 0.4832773288001198, 0.22894538706919282, 0.1999439322930615, 0.2292894166915158, 0.5539742381357069, 0.9617174662483176, 0.7582714254103564, 0.2856351792601953, 0.20167144422400596, 0.19715565282671876, 0.21886428682994608, 0.34689753980081334, 0.780263607266751]
x4 = [i / (len(y4) - 1) for i in range(0, len(y4))]
ax.plot(x1, y1, c="red", label="4th order", marker="o")
ax.plot(x2, y2, c="blue", label="8th order", marker="o")
ax.plot(x3, y3, c="green", label="12th order", marker="o")
ax.plot(x4, y4, c="yellow", label="16th order", marker="o")
ax.set_ylabel('coupling efficiency K')
ax.grid(which='both')
plt.legend(numpoints=1)

plt.show()
