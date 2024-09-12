//
//  ViewController4.swift
//  med_p
//
//  Created by Valeria on 28/05/2024.
//  Copyright © 2024 org. All rights reserved.
//

import UIKit
import AVKit
import AVFoundation

class ViewController4: UIViewController, UIImagePickerControllerDelegate, UINavigationControllerDelegate
{
        @IBOutlet weak var imagebut: UIButton!
    @IBOutlet weak var texttest: UITextView!
    let constr = UserDefaults.standard.integer(forKey: "const")

    @IBOutlet weak var name: UILabel!
    @IBOutlet weak var time: UITextView!
    @IBOutlet weak var recomendation: UITextView!
    var videoString: String!

    //@IBAction func videobutton(_ sender: UIButton) {
    //    playVideo()
    //}
    
    private func playVideo() {
        guard let path = Bundle.main.path(forResource: videoString, ofType:"mp4")
            else {
            debugPrint("video.m4v not found")
            return
        }
        let player = AVPlayer(url: URL(fileURLWithPath: path))
        let playerController = AVPlayerViewController()
        playerController.player = player
        present(playerController, animated: true)
        {
            player.play()
        }
    }
    
    @IBAction func videobut(_ sender: UIButton) {
        playVideo()
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()

        if (constr == 2) {
            recomendation.text = "Вымойте руки и аккуратно снимите каппы с зубов. Промойте элайнеры под проточной водой.С помощью специальной щетки, либо обычной щетки с мягкой щетиной почистите элайнеры. Очистите элайнеры с внутренней и внешней стороны, чтобы тщательно удалить все частички налета и пищи. Смыв все остатки пасты  водой, положите элайнеры в контейнер на время чистки зубов. Используя зубную пасту, щетку и зубную нить почистите зубы. С помощью зубной нити можно удалить налет между зубами, а также вычистить остатки пищи.Один раз в день оставляйте каппу в специальном растворе на 15 минут. Данную процедуру можно проводить утром или вечером. После дезинфекции промойте каппы в проточной воде и наденьте обратно на зубы."
            time.text = "Тщательный уход 2 раза в день, споласкивать элайнеры перед надеванием (после приема пищи)."
            name.text = "Уход за элайнерами"
            videoString = "video2"
            
        }
        if (constr == 1) {
            recomendation.text = "Демонтировать съемные конструкции, если они имеются; классической щеткой совершать круговые движения по поверхности зубов; наиболее внимательно очищать участки возле кронштейнов; прочищать межзубные промежутки с помощью зубной нити; при необходимости воспользоваться ирригатором; полоскать ротовую полость ополаскивателем. В среднем процедура занимает около 10 минут. При этом очищение должно быть одновременно и наружной, и с внутренней стороны."
            time.text = "Утром и вечером в течение 10 минут, а также по возможности после каждого приема пищи."
            name.text = "Уход за полостью рта"
            videoString = "video"
        }
        if (constr == 3) {
            recomendation.text = "После каждого приема пищи необходимо тщательно чистить зубы и прочищать аппарат щеткой с зубной пастой или мылом, затем промывать аппарат водой, обрабатывая все поверхности пластинки. Хранить пластинку нужно в сухом герметичном контейнере. Ни в коем случае пластинку нельзя хранить в воде и в других жидкостях. Обращаться с ортодонтической пластинкой аккуратно и бережно. Нельзя ронять, бросать, хранить без контейнера в сумке или в кармане."
            time.text = "После каждого приема пищи"
            name.text = "Уход за пластинкой"
            videoString = "video3"
        }
        
        if (constr == 4) {
            recomendation.text = "Вымойте руки и аккуратно снимите каппы с зубов. Промойте элайнеры под проточной водой.С помощью специальной щетки, либо обычной щетки с мягкой щетиной почистите элайнеры. Очистите элайнеры с внутренней и внешней стороны, чтобы тщательно удалить все частички налета и пищи. Смыв все остатки пасты  водой, положите элайнеры в контейнер на время чистки зубов. Используя зубную пасту, щетку и зубную нить почистите зубы. С помощью зубной нити можно удалить налет между зубами, а также вычистить остатки пищи.Один раз в день оставляйте каппу в специальном растворе на 15 минут. Данную процедуру можно проводить утром или вечером. После дезинфекции промойте каппы в проточной воде и наденьте обратно на зубы."
            time.text = "Тщательный уход 2 раза в день, споласкивать элайнеры перед надеванием (после приема пищи)."
            name.text = "Уход за трейнерами"
            videoString = "video2"
        }
    }
    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destination.
        // Pass the selected object to the new view controller.
    }
    */

}
