(import __read_csv
        [exec :as read]
)

(import __single_arg
        [exec :as arg]
)

(defn exec [[filename (arg)]]
  (list (enumerate (get (read filename) 0)))
)

(defn main []
  (exec)
)

(main)