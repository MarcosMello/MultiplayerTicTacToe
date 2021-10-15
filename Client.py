import socket;
import tkinter as tk;
from tkinter import ttk;
from tkinter import messagebox

chatOpen = False;
chatWinOBJ = None;
playersList = ["Player1", "Player2", "Player3", "Player4", "Player5", "Player6", "Player7", "Player8", "Player9", "Player10"];
leader = playersList[0]; #TMP - It'll be received as leader 
idListPlayers = [];
respOp = False;

class GUI:
    def __init__(self, root):
        self.root = root;

        root.title("Jogo da Velha - Login");
        root.iconphoto(True, tk.PhotoImage(file = 'images/icon.png'));
        root.minsize(300, 500);
        root.maxsize(300, 500); #TMP
        root.wm_attributes("-transparentcolor", 'grey');

        self.loginGUI();

    def loginGUI(self):
        l1 = tk.Label(root, text = "hi");
        l1.pack();

        root.withdraw();

    def gamewin(self):
        self.gameWin = tk.Toplevel(root);
        gameWin = self.gameWin;
        gameWin.minsize(500, 500);
        gameWin.maxsize(500, 500); #TMP
        gameWin.title("Jogo da Velha - Game");
        gameWin.protocol("WM_DELETE_WINDOW", finishGame);

        connectedto = tk.Frame(gameWin, bg = "red", height = 47, width = 350);
        connectedto.grid(column = 0, columnspan = 3, row = 0);
        connectedto.pack_propagate(False);

        self.labelC = tk.Label(connectedto, textvariable = ipaddrTxt);
        self.labelC.pack(expand = True);

        sepFr1 = tk.Frame(gameWin, height = 4, width = 350, bg = 'black');
        sepFr1.grid(column = 0, columnspan = 3, row = 1);
        sepFr1.pack_propagate(False);

        turns = tk.Frame(gameWin, bg = "blue", height = 98, width = 244);
        turns.grid(column = 0, row = 2);
        turns.pack_propagate(False);

        labelT = tk.Label(turns, textvariable = turnTxt);
        labelT.pack(expand = True);

        sepFr5 = tk.Frame(gameWin, height = 98, width = 4, bg = 'black'); #
        sepFr5.grid(column = 1, row = 2);
        sepFr5.pack_propagate(False);

        symbol = tk.Frame(gameWin, bg = "green", height = 98, width = 102);
        symbol.grid(column = 2, row = 2);
        symbol.pack_propagate(False);

        labelSymT = tk.Label(symbol, text = "Seu Simbolo:");
        labelSymT.pack(expand = True);

        labelSymS = tk.Label(symbol, textvariable = symbolTxt);
        labelSymS.pack(expand = True);

        sepFr2 = tk.Frame(gameWin, height = 4, width = 350, bg = 'black');
        sepFr2.grid(column = 0, columnspan = 3, row = 3);
        sepFr2.pack_propagate(False);

        game = tk.Frame(gameWin, bg = "yellow", height = 347, width = 350);
        game.grid(column = 0, columnspan = 3, row = 4, rowspan = 6); 

        score = tk.Frame(gameWin, bg = "purple", height = 171, width = 150);
        score.grid(column = 4, row = 0, rowspan = 5);
        score.pack_propagate(False);

        labelScore1 = tk.Label(score, text = "Placar");
        labelScore1.pack(expand = True);
        labelScore2 = tk.Label(score, textvariable = scoreTxt);
        labelScore2.pack(expand = True);

        sepFr3 = tk.Frame(gameWin, height = 4, width = 150, bg = 'black');
        sepFr3.grid(column = 4, row = 6);
        sepFr3.pack_propagate(False);

        self.playersF = tk.Frame(gameWin, bg = "brown", height = 296, width = 150);
        playersF = self.playersF;
        playersF.grid(column = 4, row = 7);
        playersF.pack_propagate(False);

        labelPlayerTitle = tk.Label(playersF, text = "PLAYERS:");
        labelPlayerTitle.pack(expand = True);

        players.update_players(playersF);

        sepFr4 = tk.Frame(gameWin, height = 4, width = 150, bg = 'black');
        sepFr4.grid(column = 4, row = 8);
        sepFr4.pack_propagate(False);

        chatFrame = tk.Frame(gameWin, bg = "teal", height = 25, width = 150);
        chatFrame.grid(column = 4, row = 9);
        chatFrame.pack_propagate(False);

        buttonChat = tk.Button(chatFrame, textvariable = chatTxt, height = 25, width = 150, command = openChat, bd = 0);
        buttonChat.pack(expand = True);

        sepFr6 = tk.Frame(gameWin, height = 500, width = 4, bg = 'black');
        sepFr6.grid(column = 3, row = 0, rowspan = 10);
        sepFr6.pack_propagate(False);

        return self;

    def chat(self):
        self.chatWin = tk.Toplevel(root);
        self.chatWin.minsize(300, 500);
        self.chatWin.maxsize(300, 500); #TMP
        self.chatWin.title("Chat");
        self.chatWin.protocol("WM_DELETE_WINDOW", handleChatState);

        hist = tk.Frame(self.chatWin, bg = "red", height = 425, width = 300);
        hist.grid(column = 0, row = 0);
        typebox = tk.Frame(self.chatWin, bg = "blue", height = 75, width = 300);
        typebox.grid(column = 0, row = 1);
        global chatOpen;
        chatOpen = True;

        return self;

class players:
    def add_player(name, master):
        if name == leader:
            labelP = tk.Label(master, text = (name + " (L)"));
            return labelP;
        else:
            labelP = tk.Label(master, text = name);
            return labelP;

    def update_players(master):
        global idListPlayers;

        for playerN in range(len(playersList)):
            if not idListPlayers:
                pID = players.add_player(playersList[playerN], master);
                idListPlayers.append(pID);
                pID.pack(expand = True);
            else:
                if len(idListPlayers)-1 < playerN:
                    pID = players.add_player(playersList[playerN], master);
                    idListPlayers.append(pID);
                    pID.pack(expand = True);

def openChat():
    if not chatOpen:
        global chatWinOBJ;
        chatWinOBJ = GUI.chat(app);
    else:
        if chatWinOBJ != None:
            chatWinOBJ.chatWin.focus_force();
            chatWinOBJ.chatWin.bell();

def handleChatState():
    global chatOpen;
    chatOpen = False;
    if chatWinOBJ != None:
        chatWinOBJ.chatWin.destroy();

def finishGame():
    resp = messagebox.askyesnocancel(title = "Atenção! - Fechar", message = "Deseja ir para tela de login?", default = 'cancel', parent = gameScrn.gameWin);

    if resp:
        gameScrn.gameWin.destroy();
        #disconnect(True); #continue? True -> try disconnect on thread and continue instantaneously
        root.deiconify();
    elif not resp and resp != None:
        #disconnect(False); #continue? False -> try disconnect on thread while show a message
        root.destroy();

root = tk.Tk();

#TMP

ipaddr = "localhost";

ipaddrTxt = tk.StringVar(value = "Conectado à: " + ipaddr);
scoreTxt = tk.StringVar(value = "1W/0L");
chatTxt = tk.StringVar(value = "(1) Chat");
symbolTxt = tk.StringVar(value = "X");
turnTxt = tk.StringVar(value = "SEU TURNO!");

#TMP

app = GUI(root);
gameScrn = GUI.gamewin(app);

root.mainloop();