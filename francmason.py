import tkinter as tk

BG_DARK, BG_PANEL, BG_CARD, BG_INPUT = "#0d0b08", "#120e08", "#1a1408", "#0a0805"
BG_BTN, BG_BTN_HOV, BG_BTN_ACT = "#221a08", "#2e2410", "#3a2e14"
GOLD, GOLD_BRIGHT, GOLD_DIM, GOLD_FAINT = "#c9b97a", "#e8d89a", "#7a6d4a", "#3a3020"
BORDER = "#2a2010"

def dibujar(canvas, n, s=50):
    canvas.delete("all")
    m, col = 10, GOLD
    t, x, y = s - m*2, m, m
    cx, cy = x + t/2, y + t/2
    L = lambda x1,y1,x2,y2: canvas.create_line(x1,y1,x2,y2, width=2, fill=col, capstyle=tk.ROUND)
    D = lambda: canvas.create_oval(cx-3,cy-3,cx+3,cy+3, fill=col, outline="")
    if 1 <= n <= 18:
        b = (n-1)%9+1
        if b in [4,5,6,7,8,9]: L(x,y,x+t,y)
        if b in [1,2,3,4,5,6]: L(x,y+t,x+t,y+t)
        if b in [2,3,5,6,8,9]: L(x,y,x,y+t)
        if b in [1,2,4,5,7,8]: L(x+t,y,x+t,y+t)
        if n > 9: D()
    elif 19 <= n <= 26:
        b = (n-19)%4
        if b==0: L(x,y,cx,y+t); L(x+t,y,cx,y+t)
        elif b==1: L(x,y,x+t,cy); L(x,y+t,x+t,cy)
        elif b==2: L(x,y+t,cx,y); L(x+t,y+t,cx,y)
        elif b==3: L(x+t,y,x,cy); L(x+t,y+t,x,cy)
        if n > 22: D()

class App:
    def __init__(self, root):
        self.root = root
        root.title("Cifrador Masónico — Pigpen")
        root.geometry("780x620")
        root.resizable(False, False)
        root.configure(bg=BG_DARK)
        self.fL = ("Courier New", 9, "bold")
        self.fI = ("Georgia", 14)
        self.fB = ("Courier New", 9, "bold")
        self.fR = ("Courier New", 22, "bold")
        self.fT = ("Courier New", 7)
        self.fS = ("Georgia", 10, "italic")
        self._build()

    def _lbl(self, p, text, font, fg, bg=None, **kw):
        return tk.Label(p, text=text, font=font, fg=fg, bg=bg or BG_PANEL, **kw)

    def _build(self):
        hdr = tk.Frame(self.root, bg=BG_DARK)
        hdr.pack(fill="x", padx=30, pady=(20,0))
        tk.Frame(hdr, bg=GOLD_FAINT, height=1).pack(fill="x", pady=(0,8))
        eye = tk.Canvas(hdr, width=50, height=42, bg=BG_DARK, highlightthickness=0)
        eye.pack()
        eye.create_polygon(25,3,48,39,2,39, outline=GOLD, fill="", width=1)
        eye.create_oval(17,22,33,36, outline=GOLD, fill="", width=1)
        eye.create_oval(22,27,28,33, fill=GOLD, outline="")
        for dx,dy in [(-8,-8),(8,-8),(0,-10)]:
            eye.create_line(25,29,25+dx,29+dy, fill=GOLD_FAINT, width=1)
        tk.Label(hdr, text="C I F R A D O R   M A S Ó N I C O",
                 font=("Georgia",18,"bold"), bg=BG_DARK, fg=GOLD_BRIGHT).pack()
        tk.Label(hdr, text="Pigpen Cipher  ·  Arte del Silencio",
                 font=("Georgia",10,"italic"), bg=BG_DARK, fg=GOLD_DIM).pack(pady=(2,8))
        tk.Frame(hdr, bg=GOLD_FAINT, height=1).pack(fill="x")

        tab_row = tk.Frame(self.root, bg=BORDER)
        tab_row.pack(fill="x", padx=30, pady=(14,0))
        self.host = tk.Frame(self.root, bg=BG_PANEL, highlightbackground=BORDER, highlightthickness=1)
        self.host.pack(fill="both", expand=True, padx=30, pady=(0,20))

        self.btns, self.panels = [], []
        for i,(lbl,fn) in enumerate([("▲  CIFRAR",self._tab_cifrar),
                                      ("▼  DESCIFRAR",self._tab_descifrar),
                                      ("◆  REFERENCIA",self._tab_ref)]):
            b = tk.Button(tab_row, text=lbl, font=self.fB, bg=BG_DARK, fg=GOLD_DIM,
                          relief="flat", activebackground=BG_CARD, activeforeground=GOLD,
                          cursor="hand2", padx=18, pady=7,
                          command=lambda i=i: self._switch(i))
            b.pack(side="left")
            self.btns.append(b)
            p = tk.Frame(self.host, bg=BG_PANEL)
            fn(p)
            self.panels.append(p)
        self._switch(0)

    def _switch(self, idx):
        for i,(b,p) in enumerate(zip(self.btns, self.panels)):
            if i == idx:
                b.config(bg=BG_CARD, fg=GOLD_BRIGHT)
                p.pack(fill="both", expand=True)
            else:
                b.config(bg=BG_DARK, fg=GOLD_DIM)
                p.pack_forget()

    def _btn(self, parent, text, cmd, side="left", ghost=False):
        bg, fg = (BG_DARK, GOLD_DIM) if ghost else (BG_BTN, GOLD)
        b = tk.Button(parent, text=text, command=cmd, font=self.fB, bg=bg, fg=fg,
                      activebackground=BG_BTN_ACT, activeforeground=GOLD_BRIGHT,
                      relief="flat", highlightbackground=BORDER, highlightthickness=1,
                      cursor="hand2", padx=12, pady=5)
        b.pack(side=side, padx=(0,6))
        b.bind("<Enter>", lambda e: b.config(bg=BG_BTN_HOV, fg=GOLD))
        b.bind("<Leave>", lambda e: b.config(bg=bg, fg=fg))
        return b

    def _symbol_grid(self, parent, num, clickable=False):
        cell = tk.Frame(parent, bg=BG_CARD, highlightbackground=BORDER,
                        highlightthickness=1, cursor="hand2" if clickable else "")
        c = tk.Canvas(cell, width=50, height=50, bg=BG_CARD, highlightthickness=0)
        c.pack(padx=2, pady=(2,0))
        dibujar(c, num)
        lbl = tk.Label(cell, text=chr(64+num), font=self.fT, bg=BG_CARD, fg=GOLD_DIM)
        lbl.pack(pady=(0,2))
        if clickable:
            def on_enter(e): cell.config(highlightbackground=GOLD_DIM); c.config(bg=BG_BTN_HOV); lbl.config(bg=BG_BTN_HOV)
            def on_leave(e): cell.config(highlightbackground=BORDER); c.config(bg=BG_CARD); lbl.config(bg=BG_CARD)
            def on_click(e): self.lbl_res.config(text=self.lbl_res.cget("text")+chr(64+num))
            for w in (cell, c, lbl):
                w.bind("<Enter>", on_enter); w.bind("<Leave>", on_leave); w.bind("<Button-1>", on_click)
        return cell

    def _tab_cifrar(self, parent):
        inn = tk.Frame(parent, bg=BG_PANEL)
        inn.pack(fill="both", expand=True, padx=20, pady=16)
        self._lbl(inn, "MENSAJE A CIFRAR", self.fL, GOLD_DIM).pack(anchor="w", pady=(0,4))
        row = tk.Frame(inn, bg=BG_PANEL)
        row.pack(fill="x", pady=(0,14))
        self.entry = tk.Entry(row, font=self.fI, bg=BG_INPUT, fg=GOLD_BRIGHT,
                              insertbackground=GOLD, relief="flat", highlightthickness=1,
                              highlightcolor=GOLD, highlightbackground=BORDER, width=28)
        self.entry.pack(side="left", ipady=6, padx=(0,8))
        self.entry.bind("<KeyRelease>", self._cifrar)
        self._btn(row, "CIFRAR", self._cifrar)
        self._btn(row, "LIMPIAR", lambda: [self.entry.delete(0,tk.END), self._cifrar()], ghost=True)
        self._lbl(inn, "SÍMBOLOS GENERADOS", self.fL, GOLD_DIM).pack(anchor="w", pady=(0,6))
        cont = tk.Frame(inn, bg=BG_INPUT, highlightbackground=BORDER, highlightthickness=1)
        cont.pack(fill="both", expand=True)
        self.sc = tk.Canvas(cont, bg=BG_INPUT, highlightthickness=0, height=220)
        sb = tk.Scrollbar(cont, orient="horizontal", command=self.sc.xview, bg=BG_CARD)
        self.sc.configure(xscrollcommand=sb.set)
        sb.pack(side="bottom", fill="x")
        self.sc.pack(fill="both", expand=True)
        self.fsym = tk.Frame(self.sc, bg=BG_INPUT)
        self.sc.create_window((0,0), window=self.fsym, anchor="nw")
        self.fsym.bind("<Configure>", lambda e: self.sc.configure(scrollregion=self.sc.bbox("all")))
        self._lbl(self.fsym, "\n— Los símbolos aparecerán aquí —\n", self.fS, GOLD_FAINT, BG_INPUT).pack(padx=20, pady=60)

    def _cifrar(self, event=None):
        nums = [ord(c)-64 for c in self.entry.get().upper() if c.isalpha()]
        for w in self.fsym.winfo_children(): w.destroy()
        if not nums:
            self._lbl(self.fsym, "\n— Los símbolos aparecerán aquí —\n", self.fS, GOLD_FAINT, BG_INPUT).pack(padx=20, pady=60)
            return
        wrap = tk.Frame(self.fsym, bg=BG_INPUT)
        wrap.pack(padx=10, pady=10)
        for i,n in enumerate(nums):
            cell = tk.Frame(wrap, bg=BG_CARD, highlightbackground=BORDER, highlightthickness=1)
            cell.grid(row=i//10, column=i%10, padx=4, pady=4)
            c = tk.Canvas(cell, width=50, height=50, bg=BG_CARD, highlightthickness=0)
            c.pack(padx=2, pady=2)
            dibujar(c, n)

    def _tab_descifrar(self, parent):
        inn = tk.Frame(parent, bg=BG_PANEL)
        inn.pack(fill="both", expand=True, padx=20, pady=16)
        self._lbl(inn, "MENSAJE DESCIFRADO", self.fL, GOLD_DIM).pack(anchor="w", pady=(0,4))
        df = tk.Frame(inn, bg=BG_INPUT, highlightbackground=GOLD_FAINT, highlightthickness=1)
        df.pack(fill="x", pady=(0,10))
        self.lbl_res = tk.Label(df, text="", font=self.fR, bg=BG_INPUT, fg=GOLD_BRIGHT,
                                anchor="w", padx=14, pady=10, height=1)
        self.lbl_res.pack(fill="x")
        br = tk.Frame(inn, bg=BG_PANEL)
        br.pack(fill="x", pady=(0,14))
        self._btn(br, "⌫  BORRAR", lambda: self.lbl_res.config(text=self.lbl_res.cget("text")[:-1]))
        self._btn(br, "LIMPIAR", lambda: self.lbl_res.config(text=""), ghost=True)
        self._lbl(inn, "TECLADO — HAZ CLIC EN EL SÍMBOLO", self.fL, GOLD_DIM).pack(anchor="w", pady=(0,8))
        gf = tk.Frame(inn, bg=BG_PANEL)
        gf.pack(anchor="w")
        for i in range(1,27):
            self._symbol_grid(gf, i, clickable=True).grid(row=(i-1)//9, column=(i-1)%9, padx=3, pady=3)

    def _tab_ref(self, parent):
        inn = tk.Frame(parent, bg=BG_PANEL)
        inn.pack(fill="both", expand=True, padx=20, pady=16)
        self._lbl(inn, "TABLA DE REFERENCIA — A→Z", self.fL, GOLD_DIM).pack(anchor="w", pady=(0,10))
        gf = tk.Frame(inn, bg=BG_PANEL)
        gf.pack(anchor="w")
        for i in range(1,27):
            self._symbol_grid(gf, i).grid(row=(i-1)//9, column=(i-1)%9, padx=3, pady=3)
        tk.Frame(inn, bg=GOLD_FAINT, height=1).pack(fill="x", pady=(16,10))
        tk.Label(inn, text="A–I: cuadrícula sin punto  ·  J–R: cuadrícula + punto  ·  S–V: cruces  ·  W–Z: cruces + punto",
                 font=("Courier New",8), bg=BG_PANEL, fg=GOLD_DIM, wraplength=680, justify="left").pack(anchor="w")

if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()