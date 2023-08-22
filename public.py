import sys
import cv2


def delay_key(i):
    key = cv2.waitKey(i)
    if key == ord('q'):
        cv2.destroyAllWindows()
        sys.exit(0)
    elif key == ord('p'):
        key = cv2.waitKey(0)
        while key != ord('c'):
            if key == ord('q'):
                cv2.destroyAllWindows()
                sys.exit(0)
            key = cv2.waitKey(0)