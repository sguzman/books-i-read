(import __single_arg
 [exec :as arg]
)

(defn exec []
 ""
 (arg)
)

(defn main []
 (print (arg))
)

(if (= __name__ "__main__")
 (main)
)