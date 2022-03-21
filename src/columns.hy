(import __read_csv
  [exec :as read]
)

(import __single_arg
  [exec :as arg]
)

(import __single_arg
  [exec :as arg]
)

(defn exec [filename]
  (list (enumerate (get (read filename) 0)))
)

(defn main []
  (for [row  (exec (arg))]
    (print (get row 0) (get row 1))
  )
)

(main)
