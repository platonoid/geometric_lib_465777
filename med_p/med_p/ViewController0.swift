//
//  ViewController0.swift
//  med_p
//
//  Created by Valeria on 28/05/2024.
//  Copyright © 2024 org. All rights reserved.
//

import UIKit

class ViewController0: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
    }
    
    @IBAction func brec(_ sender: UIButton) {
        UserDefaults.standard.set(1, forKey: "const")
    }
    
    
    @IBAction func elayner(_ sender: UIButton) {
        UserDefaults.standard.set(2, forKey: "const")
    }
    
    @IBAction func plast(_ sender: UIButton) {
        UserDefaults.standard.set(3, forKey: "const")
    }
    
    @IBAction func treiner(_ sender: UIButton) {
        UserDefaults.standard.set(4, forKey: "const")
    }
    /*
    // MARK: - Navigation

     @IBAction func ela(_ sender: Any) {
     }
     // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destination.
        // Pass the selected object to the new view controller.
    }
    */

}
