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
turn = True;

p = True;

al = [True, True, True, True, True, True, True, True, True];

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
        game.pack_propagate(False);

        quad1 = tk.Frame(game, bg = "yellow", height = 115, width = 116);

        quad1.grid(column = 0, row = 0);

        quad1.pack_propagate(False);
        lquad1 = tk.Label(quad1, textvariable = lquad1Txt, bg = "yellow");
        lquad1.pack(expand = True);

        quad1.bind("<Button-1>", lambda event: click(event, 1) if (turn and al[0]) else None);

        hv1 = tk.Frame(game, bg = "black", height = 115, width = 1);
        hv1.grid(column = 1, row = 0);

        quad2 = tk.Frame(game, bg = "yellow", height = 115, width = 116);

        quad2.grid(column = 2, row = 0);

        quad2.pack_propagate(False);
        lquad2 = tk.Label(quad2, textvariable = lquad2Txt, bg = "yellow");
        lquad2.pack(expand = True);

        quad2.bind("<Button-1>", lambda event: click(event, 2) if (turn and al[1]) else None);

        hv2 = tk.Frame(game, bg = "black", height = 115, width = 1);
        hv2.grid(column = 3, row = 0);

        quad3 = tk.Frame(game, bg = "yellow", height = 115, width = 116);

        quad3.grid(column = 4, row = 0);

        quad3.pack_propagate(False);
        lquad3 = tk.Label(quad3, textvariable = lquad3Txt, bg = "yellow");
        lquad3.pack(expand = True);

        quad3.bind("<Button-1>", lambda event: click(event, 3) if (turn and al[2]) else None);

        hh1 = tk.Frame(game, bg = "black", height = 1, width = 350);
        hh1.grid(column = 0, row = 1, columnspan = 5);

        quad4 = tk.Frame(game, bg = "yellow", height = 115, width = 116);

        quad4.grid(column = 0, row = 2);

        quad4.pack_propagate(False);
        lquad4 = tk.Label(quad4, textvariable = lquad4Txt, bg = "yellow");
        lquad4.pack(expand = True);

        quad4.bind("<Button-1>", lambda event: click(event, 4) if (turn and al[3]) else None);

        hv3 = tk.Frame(game, bg = "black", height = 115, width = 1);
        hv3.grid(column = 1, row = 2);

        quad5 = tk.Frame(game, bg = "yellow", height = 115, width = 116);

        quad5.grid(column = 2, row = 2);

        quad5.pack_propagate(False);
        lquad5 = tk.Label(quad5, textvariable = lquad5Txt, bg = "yellow");
        lquad5.pack(expand = True);

        quad5.bind("<Button-1>", lambda event: click(event, 5) if (turn and al[4]) else None);

        hv4 = tk.Frame(game, bg = "black", height = 115, width = 1);
        hv4.grid(column = 3, row = 2);

        quad6 = tk.Frame(game, bg = "yellow", height = 115, width = 116);

        quad6.grid(column = 4, row = 2);

        quad6.pack_propagate(False);
        lquad6 = tk.Label(quad6, textvariable = lquad6Txt, bg = "yellow");
        lquad6.pack(expand = True);

        quad6.bind("<Button-1>", lambda event: click(event, 6) if (turn and al[5]) else None);

        hh2 = tk.Frame(game, bg = "black", height = 1, width = 350);
        hh2.grid(column = 0, row = 3, columnspan = 5);

        quad7 = tk.Frame(game, bg = "yellow", height = 115, width = 116);

        quad7.grid(column = 0, row = 4);

        quad7.pack_propagate(False);
        lquad7 = tk.Label(quad7, textvariable = lquad7Txt, bg = "yellow");
        lquad7.pack(expand = True);

        quad7.bind("<Button-1>", lambda event: click(event, 7) if (turn and al[6]) else None);

        hv5 = tk.Frame(game, bg = "black", height = 115, width = 1);
        hv5.grid(column = 1, row = 4);

        quad8 = tk.Frame(game, bg = "yellow", height = 115, width = 116);

        quad8.grid(column = 2, row = 4);

        quad8.pack_propagate(False);
        lquad8 = tk.Label(quad8, textvariable = lquad8Txt, bg = "yellow");
        lquad8.pack(expand = True);

        quad8.bind("<Button-1>", lambda event: click(event, 8) if (turn and al[7]) else None);

        hv6 = tk.Frame(game, bg = "black", height = 115, width = 1);
        hv6.grid(column = 3, row = 4);

        quad9 = tk.Frame(game, bg = "yellow", height = 115, width = 116);

        quad9.grid(column = 4, row = 4);

        quad9.pack_propagate(False);
        lquad9 = tk.Label(quad9, textvariable = lquad9Txt, bg = "yellow");
        lquad9.pack(expand = True);

        quad9.bind("<Button-1>", lambda event: click(event, 9) if (turn and al[8]) else None);

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

def click(event, quad):
    global p;

    if p: 
        lquads[quad-1].set("X");
        p = not p;
        al[quad-1] = False;
    else:
        lquads[quad-1].set("O");
        p = not p;
        al[quad-1] = False;

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

lquad1Txt = tk.StringVar(value = "");
lquad2Txt = tk.StringVar(value = "");
lquad3Txt = tk.StringVar(value = "");
lquad4Txt = tk.StringVar(value = "");
lquad5Txt = tk.StringVar(value = "");
lquad6Txt = tk.StringVar(value = "");
lquad7Txt = tk.StringVar(value = "");
lquad8Txt = tk.StringVar(value = "");
lquad9Txt = tk.StringVar(value = "");

lquads = [lquad1Txt, lquad2Txt, lquad3Txt, lquad4Txt, lquad5Txt, lquad6Txt, lquad7Txt, lquad8Txt, lquad9Txt];

app = GUI(root);
gameScrn = GUI.gamewin(app);

root.mainloop();