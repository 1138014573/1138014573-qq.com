#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
import json
import time
import common.getCoinQuotes
from os import path 


class PrinterTkinter:
    def __init__(self):
        self.root = Tk()
        self.root.title("虚拟货币行情")
        self.path = path.dirname(__file__).replace("\\","/")
        self.root.iconbitmap(self.path + "/static/logo.ico")

        self.frame_left_top = Frame(width=400, height=200)
        self.frame_right_top = Frame(width=400, height=200)
        self.frame_center = Frame(width=800, height=400)
        self.frame_bottom = Frame(width=800, height=50)

        # 定义中心列表区域
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=18, columns=("a", "b", "c", "d", "e"))
        self.vbar = ttk.Scrollbar(self.frame_center, orient=VERTICAL, command=self.tree.yview)
        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)

        # 表格的标题
        self.tree.column("a", width=50, anchor="center")
        self.tree.column("b", width=200, anchor="center")
        self.tree.column("c", width=200, anchor="center")
        self.tree.column("d", width=100, anchor="center")
        self.tree.column("e", width=150, anchor="center")
        self.tree.heading("a", text="币种")
        self.tree.heading("b", text="价格usd")
        self.tree.heading("c", text="价格rmb")
        self.tree.heading("d", text="24h涨跌")
        self.tree.heading("e", text="更新时间")

        # 调用方法获取表格内容插入
        self.get_tree()
        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)

        # 整体区域定位
        self.frame_center.grid(row=1, column=0, columnspan=2, padx=4, pady=5)
        self.frame_bottom.grid(row=2, column=0, columnspan=2)

        self.frame_left_top.grid_propagate(0)
        self.frame_right_top.grid_propagate(0)
        self.frame_center.grid_propagate(0)
        self.frame_bottom.grid_propagate(0)

        self.root.mainloop()

    # 表格内容插入
    def get_tree(self):
        # 删除原节点
        for _ in map(self.tree.delete, self.tree.get_children("")):
            pass
        # 更新插入新节点
        res = self.loadFont()
        line = 0
        for i in res: # 写入数据
            dataTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(i['last_updated']))
            priceRmb = i['price_usd'] * 7.1
            priceRmb = str(priceRmb).split('.')[0] + '.' + str(priceRmb).split('.')[1][:2]
            self.tree.insert('', line, values=(i['symbol'], i['price_usd'],priceRmb,i['percent_change_24h'],dataTime))
            line =+ line
        self.tree.after(60000, self.get_tree)

    def loadFont(self):
        res = common.getCoinQuotes.Coin().getCoinList()
        return res

if __name__ == '__main__':
    PrinterTkinter()
