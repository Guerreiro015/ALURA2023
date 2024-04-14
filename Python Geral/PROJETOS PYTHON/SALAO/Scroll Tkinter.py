import tkinter as tk

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.frame = tk.Frame(self)
        self.frame.grid(row=0, column=0, sticky='NW')

        cellYScrollbar = tk.Scrollbar(self, orient="vertical")
        cellXScrollbar = tk.Scrollbar(self, orient="horizontal")
        full_width = 50

        self.cell = tk.Text(
            self,
            yscrollcommand=cellYScrollbar.set,
            xscrollcommand=cellXScrollbar.set,
            width=full_width,
            height=full_width // 2,
            wrap="none",
            cursor="arrow"
        )

        cellYScrollbar.config(command=self.cell.yview)
        cellXScrollbar.config(command=self.cell.xview)

        self.cell.grid(row=0, column=0, sticky='NW', padx=[5, 0], pady=[5, 0])
        cellXScrollbar.grid(row=1, column=0, columnspan=2, sticky='NEW', padx=[5, 0], pady=[0, 5])
        cellYScrollbar.grid(row=0, column=1, sticky='NSW', padx=[0, 5], pady=[5, 0])

        tiles = []
        for i in range(0, 9):
            for j in range(0, 9):
                test = tk.Label(self.cell, text=('INDICE','NOME','CPF','TELEFONE','E-MAIL','CADASTRO','CEP','RUA','NÚMERO','BAIRRO','CIDADE','UF',
                   'DDD','SERVIÇO','DATA SERVIÇO', 'Vlr. SERVICO','Quant. PARCELAS','Vlr. PARCELAS','% COMISSÃO','Vlr. COMISSÃO','FORMA DE PG'), width=200, height=3)
                tiles.append(test)
                self.cell.window_create("end", window=test, padx=1, pady=1)
                self.cell.insert("end", "\n")

        for tile in tiles:
            tile.bind("<MouseWheel>", lambda event: self.cell.yview_scroll(int(-1 * (event.delta / 120)), "units"))

        self.cell.config(state='disabled')

if __name__ == "__main__":
    root = App()
    root.mainloop()
    
    