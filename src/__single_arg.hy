(import sys)

(defn exec [n]
 (get (. sys argv) n))
