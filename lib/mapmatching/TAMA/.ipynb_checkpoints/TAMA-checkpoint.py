

class mapmatching:

    # コンストラクタ
    def __init__(self, x, y, links):
        self.x = x
        self.y = y
        self.links = links

    # 歩行座標に対して最も近い通路を探索
    def find_link(self):
        link_list=[]
        for x0,y0 in zip(self.x,self.y):
            d_list = []
            for link in self.links:
                a = link[1][0] - link[0][0]
                b = link[1][1] - link[0][1]
                r2 = a * a + b * b
                tt = -(a * (link[0][0] - x0) + b * (link[0][1] - y0))
                if tt < 0:
                    d_list.append((link[0][0] - x0) * (link[0][0] - x0) + (link[0][1] - y0) * (link[0][1] - y0))
                    print(1)
                elif tt > r2:
                    d_list.append((link[1][0] - x0) * (link[1][0] - x0) + (link[1][1] - y0) * (link[1][1] - y0))
                    print(2)
                else:
                    f1 = a * (link[0][1] - y0) - b * (link[0][0] - x0)
                    d_list.append((f1 * f1) / r2)
                    print(3)
        link_list.append(d_list.index(min(d_list)))
        return link_list

    #point to curveで歩行座標を修正
    def point_to_curve(self):
        link_list=self.find_link()
        modified=[]
        for x0,y0,l in zip(self.x,self.y,link_list):
            x_l0= self.links[l][0][0]
            x_l1 = self.links[l][1][0]
            y_l0 = self.links[l][0][1]
            y_l1 = self.links[l][1][1]
            a = x_l1 - x_l0
            b = y_l1 - y_l0
            r2 = a * a + b * b
            tt = -(a * (x_l0 - x0) + b * (y_l0 - y0))
            if tt < 0:
                modified.append(self.links[l][0])
            elif tt > r2:
                modified.append(self.links[l][1])
            else:
                #f1 = a * (y_l0 - y0) - b * (x_l0 - x0)
                #d_list.append((f1 * f1) / r2)
                a_v=b
                b_v=-a
                c_v=-b*x_l0+a*y_l0
                x_v=((b_v*b_v*x0)/(a_v*a_v)+(b_v*b_v))-(b_v*y0)/(a_v+(b_v*b_v)/a_v)-c_v/(a_v+(b_v*b_v)/a_v)
                y_v=(b_v*x/a)-(b_v*x0/a_v)+y0
                modified.append([x_v,y_v])
        return modified



