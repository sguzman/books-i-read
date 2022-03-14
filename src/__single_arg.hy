(import sys)

(defn exec [[n 1]]
 (get (. sys argv) n))
