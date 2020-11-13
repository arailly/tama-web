import numpy as np
import matplotlib.pyplot as plt
import math
import random

class MapMatching:
    # コンストラクタ
    def __init__(self, x, y, links):
        """
        :param x: 歩行座標のx座標リスト
        :param y: 歩行座標のy座標リスト
        :param links: 経路座標を[[[xbegin,ybegin],[xend,yend]]...]としてリストに格納
        """
        self.x = x
        self.y = y
        self.links = links

    # 歩行座標に対して最も近い通路を探索
    def find_link(self, x_list, y_list):
        """
        rot_degを行った歩行座標に対して最も距離の近い経路を探索

        :param x_list: rot_degから出力された歩行座標のx座標
        :param y_list: rot_degから出力された歩行座標のy座標
        :return: 歩行座標のマッチング候補経路番号のリスト
        """
        link_list = []
        for x0, y0 in zip(x_list, y_list):
            d_list = []
            for link in self.links:
                x_l0 = link[0][0]
                x_l1 = link[1][0]
                y_l0 = link[0][1]
                y_l1 = link[1][1]
                a = x_l1 - x_l0
                b = y_l1 - y_l0
                if a == 0:
                    if y0 < min([y_l0, y_l1]):
                        d_list.append(((x_l0 - x0) * (x_l0 - x0) + (min([y_l0, y_l1]) - y0) * (min([y_l0, y_l1]) - y0)))
                    elif y0 > max([y_l0, y_l1]):
                        d_list.append(((x_l0 - x0) * (x_l0 - x0) + (max([y_l0, y_l1]) - y0) * (max([y_l0, y_l1]) - y0)))
                    else:
                        d_list.append(abs(x_l0 - x0))
                elif b == 0:
                    if x0 < min([x_l0, x_l1]):
                        d_list.append(((min([x_l0, x_l1]) - x0) * (min([x_l0, x_l1]) - x0) + (y_l0 - y0) * (y_l0 - y0)))
                    elif x0 > max([x_l0, x_l1]):
                        d_list.append(((max([x_l0, x_l1]) - x0) * (max([x_l0, x_l1]) - x0) + (y_l0 - y0) * (y_l0 - y0)))
                    else:
                        d_list.append(abs(y_l0 - y0))
                else:
                    s = a * (x_l1 - x0) + b * (y_l1 - y0)
                    t = a * (x_l0 - x0) + b * (y_l0 - y0)
                    if s * t <= 0:
                        p1 = np.array([x_l0, y_l0])
                        p2 = np.array([x_l1, y_l1])
                        P = np.array([x0, y0])
                        v = (p2 - p1) / np.linalg.norm(p2 - p1) 
                        h = (P - p1) @ v * v + p1 
                        d_list.append((h[0] - P[0]) * (h[0] - P[0]) + (h[1] - P[1]) * (h[1] - P[1]))
                    if s * t > 0:
                        d_list.append(min(
                            [((link[0][0] - x0) * (link[0][0] - x0) + (link[0][1] - y0) * (link[0][1] - y0)),
                             ((link[1][0] - x0) * (link[1][0] - x0) + (link[1][1] - y0) * (link[1][1] - y0))]))
            link_list.append(d_list.index(min(d_list)))
        return link_list

    # map matching関数
    def point_to_curve(self):
        """
        point_to_curveにより歩行座標を最も近い経路上に座標を修正
        :return: マップマッチングした歩行座標
        """
        x_list, y_list = self.rot_deg()
        link_list = self.find_link(x_list, y_list)
        for link in self.links:
            plt.scatter(link[0][0], link[0][1])
            plt.scatter(link[1][0], link[1][1])
        # for x_c, y_c in zip(x_list, y_list):
        #     plt.scatter(x_c, y_c)
        # plt.show()
        modified = []
        for x0, y0, l in zip(x_list, y_list, link_list):
            x_l0 = self.links[l][0][0]
            x_l1 = self.links[l][1][0]
            y_l0 = self.links[l][0][1]
            y_l1 = self.links[l][1][1]
            
            a = x_l1 - x_l0
            b = y_l1 - y_l0
            if a == 0:
                if y0 < min([y_l0, y_l1]):
                    modified.append([x_l0, min([y_l0, y_l1])])
                elif y0 > max([y_l0, y_l1]):
                    modified.append([x_l0, max([y_l0, y_l1])])
                else:
                    modified.append([x_l0, y0])
            elif b == 0:
                if x0 < min([x_l0, x_l1]):
                    modified.append([min([x_l0, x_l1]), y_l0])
                elif x0 > max([x_l0, x_l1]):
                    modified.append([max([x_l0, x_l1]), y_l0])
                else:
                    modified.append([x0, y_l0])
            else:
                s = a * (x_l1 - x0) + b * (y_l1 - y0)
                t = a * (x_l0 - x0) + b * (y_l0 - y0)
                if s * t <= 0:
                    p1 = np.array([x_l0, y_l0])
                    p2 = np.array([x_l1, y_l1])
                    P = np.array([x0, y0])
                    v = (p2 - p1) / np.linalg.norm(p2 - p1) 
                    h = (P - p1) @ v * v + p1
                    modified.append(h)
                if s * t > 0:
                    if ((link[0][0] - x0) * (link[0][0] - x0) + (link[0][1] - y0) * (link[0][1] - y0)) > (
                            (link[1][0] - x0) * (link[1][0] - x0) + (link[1][1] - y0) * (link[1][1] - y0)):
                        modified.append(self.links[l][1])
                        print(1)
                    else:
                        modified.append(self.links[l][0])
                        print(1)
        return modified

    # 座標軸を回転して調整
    def rot_deg(self):
        """
        AR COREで取得した座標の座標軸を修正
        :return:修正した歩行座標リスト
        """
        x_dash = []
        y_dash = []
        x_result = []
        y_result = []
        c = 0
        for x_c, y_c in zip(self.x, self.y):
            if ((x_c <= 0) & (y_c < 0)):
                x_dash.append(x_c)
                y_dash.append(y_c)
                c -= 1
            elif ((x_c > 0) & (y_c >= 0)):
                x_dash.append(x_c)
                y_dash.append(y_c)
                c += 1
        min_deg = 0
        for x_m, y_m in zip(x_dash, y_dash):
            if ((c > 0) & (x_m < 0)) | ((c < 0) & (y_m > 0)):
                continue
            elif c < 0:
                atan = -np.arctan(y_m / x_m) * 180 / math.pi
                print(atan)
                if atan < min_deg:
                    min_deg = atan
            else:
                atan = 90 - np.arctan(y_m / x_m) * 180 / math.pi
                if atan > min_deg:
                    min_deg = atan
        deg = np.deg2rad(min_deg)
        cos = np.cos(deg)
        sin = np.sin(deg)
        for x_c, y_c in zip(self.x, self.y):
            rot_x = (x_c * cos) - (y_c * sin)
            rot_y = (x_c * sin) + (y_c * cos)
            x_result.append(rot_x)
            y_result.append(rot_y)
        return [x_result, y_result]

