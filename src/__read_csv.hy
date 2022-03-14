(import csv
        [reader :as read])
(import __single_arg
        [exec :as arg])

(defn exec [[filename (arg)]]
  (list (read (open filename))))
