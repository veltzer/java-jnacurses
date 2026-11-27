#include<curses.h>

int gety(WINDOW *win) {
	return getcury(win);
}
int getx(WINDOW *win) {
	return getcurx(win);
}
WINDOW* getStdscr(void) {
	return stdscr;
}
int getLINES(void) {
	return LINES;
}
int getCOLS(void) {
	return COLS;
}
