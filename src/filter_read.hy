(import __read_csv
        [exec :as read])
(import __single_arg
        [exec :as arg])

(defn exec [filename]
  filename)

(defn main []
  (print (exec (arg))))

(if (= __name__ "main")
  (main))
